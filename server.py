from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure OpenAI
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("No API key found. Please set OPENAI_API_KEY in your .env file")

client = OpenAI(api_key=api_key)

@app.route('/chat', methods=['POST'])
def chat():
    try:
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