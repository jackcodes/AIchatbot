# AI Chatbot with Excel Analysis

A web-based chatbot that can analyze Excel files and provide insights using OpenAI's GPT model.

## Features

- Chat interface for general queries
- Excel file analysis capabilities
- Data insights and statistics
- Natural language responses about data patterns

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Modern web browser

## Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/ai-excel-chatbot.git
cd ai-excel-chatbot
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Unix or MacOS:
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Start the Flask server:
```bash
python server.py
```

2. In a new terminal, start the HTTP server:
```bash
python -m http.server 8000
```

3. Open your web browser and navigate to:
```
http://localhost:8000
```

4. To analyze an Excel file:
   - Click the "Upload Excel File" button
   - Select your Excel file (.xlsx or .xls)
   - Type your question about the data
   - Click Send or press Enter

## Project Structure

- `index.html`: Frontend interface
- `script.js`: Frontend JavaScript code
- `server.py`: Flask backend server
- `requirements.txt`: Python dependencies
- `.env`: Environment variables (not included in repository)
- `.gitignore`: Git ignore rules

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 