from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
from dotenv import load_dotenv
import pandas as pd
import json
import tempfile

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure OpenAI
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("No API key found. Please set OPENAI_API_KEY in your .env file")

client = OpenAI(api_key=api_key)

def analyze_excel(file_path):
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)
        
        # Get basic information about the dataset
        info = {
            "rows": len(df),
            "columns": len(df.columns),
            "column_names": df.columns.tolist(),
            "summary": df.describe().to_dict(),
            "missing_values": df.isnull().sum().to_dict()
        }
        
        return info
    except Exception as e:
        return {"error": str(e)}

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Check if a file was uploaded
        if 'file' in request.files:
            file = request.files['file']
            message = request.form.get('message', '')
            
            if file.filename == '':
                return jsonify({"error": "No file selected"}), 400
                
            if not file.filename.endswith(('.xlsx', '.xls')):
                return jsonify({"error": "Please upload an Excel file (.xlsx or .xls)"}), 400
            
            # Save the uploaded file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as temp_file:
                file.save(temp_file.name)
                analysis = analyze_excel(temp_file.name)
            
            # Clean up the temporary file
            os.unlink(temp_file.name)
            
            if "error" in analysis:
                return jsonify({"response": f"Error analyzing Excel file: {analysis['error']}"})
            
            # Create a prompt for the AI to explain the analysis
            prompt = f"""Please analyze this Excel data and provide insights:
            - Number of rows: {analysis['rows']}
            - Number of columns: {analysis['columns']}
            - Column names: {', '.join(analysis['column_names'])}
            - Summary statistics: {json.dumps(analysis['summary'], indent=2)}
            - Missing values: {json.dumps(analysis['missing_values'], indent=2)}
            
            User question: {message}
            
            Please provide a clear explanation of the data structure and any notable patterns or issues, addressing the user's question if possible."""
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a data analysis expert. Provide clear, concise insights about the data."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            return jsonify({
                "response": response.choices[0].message.content
            })
        
        # Handle regular chat messages
        data = request.json
        if not data or 'message' not in data:
            return jsonify({"error": "No message provided"}), 400
            
        message = data['message']
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful and friendly AI assistant."
                },
                {
                    "role": "user",
                    "content": message
                }
            ],
            temperature=0.7,
            max_tokens=150
        )
        
        return jsonify({
            "response": response.choices[0].message.content
        })
    except Exception as e:
        print(f"Error: {str(e)}")  # Add logging
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Starting server...")
    print(f"API Key loaded: {'Yes' if api_key else 'No'}")
    app.run(debug=True, port=5000) 