# AI Chatbot with OpenAI

A simple web-based chatbot using OpenAI's GPT-3.5 API. This project demonstrates how to create an interactive chat interface that communicates with OpenAI's language model.

## Features

- Clean, modern UI
- Real-time chat interface
- OpenAI GPT-3.5 integration
- Responsive design
- Error handling

## Setup

1. Clone the repository:
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Create a virtual environment and activate it:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your-api-key-here
```

5. Start the backend server:
```bash
python server.py
```

6. In a new terminal, start the frontend server:
```bash
python -m http.server 8000
```

7. Open your browser and go to `http://localhost:8000`

## Project Structure

- `index.html`: Frontend interface
- `script.js`: Frontend JavaScript code
- `server.py`: Backend Flask server
- `requirements.txt`: Python dependencies
- `.env`: Environment variables (not included in repository)

## Security Note

Never commit your `.env` file or expose your API key. The `.env` file is included in `.gitignore` for this reason.

## License

MIT License 