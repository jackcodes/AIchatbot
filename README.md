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
git clone https://github.com/jackcodes/AIchatbot.git
cd AIchatbot
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

4. Create a `.env` file in the root directory:

   **Method 1 - Using a text editor:**
   1. Open any text editor (like Notepad, VS Code, etc.)
   2. Create a new file
   3. Add this line (replace with your actual API key):
   ```
   OPENAI_API_KEY=your-api-key-here
   ```
   4. Save it as `.env` (make sure it's not `.env.txt`)

   **Method 2 - Using the command line:**

   On Windows (PowerShell):
   ```powershell
   echo "OPENAI_API_KEY=your-api-key-here" > .env
   ```

   On Windows (Command Prompt):
   ```cmd
   echo OPENAI_API_KEY=your-api-key-here > .env
   ```

   On Mac/Linux:
   ```bash
   echo "OPENAI_API_KEY=your-api-key-here" > .env
   ```

   **Important Notes:**
   - Make sure the `.env` file is in the root directory of the project
   - The file name must be exactly `.env` (not `.env.txt` or anything else)
   - Don't share your API key with others
   - The `.env` file is already in `.gitignore`, so it won't be pushed to GitHub

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