# 20 Questions AI Game

A simple web-based 20 Questions game where an AI thinks of an object and you try to guess it by asking yes/no questions.

## Features

- 🤖 Powered by OpenAI's GPT-4o-mini
- 💬 Clean, interactive chat interface built with Shiny for Python
- 🎮 Classic 20 Questions gameplay with reversed roles (AI thinks, you guess)
- 🚀 Simple, lightweight implementation

## Requirements

- Python 3.10+
- OpenAI API key

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd 20-questions-ai-game
```

2. Create and activate a virtual environment (recommended):
```bash
conda create -n 20questions python=3.10
conda activate 20questions
```

3. Install dependencies:
```bash
pip install shiny shinychat chatlas python-dotenv
```

4. Create a `.env` file in the project root:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

Run the app:
```bash
shiny run app.py
```

Or specify a custom port:
```bash
shiny run --port 3838 app.py
```

Then open your browser to `http://localhost:8000` (or your specified port).

## How to Play

1. The AI will think of a common object, animal, person, or place
2. You ask yes/no questions to try to guess what it is
3. You have up to 20 questions
4. If you guess correctly, you win! If not, the AI reveals the answer

## Technologies

- [Shiny for Python](https://shiny.posit.co/py/) - Web framework
- [shinychat](https://github.com/posit-dev/shinychat) - Chat UI components
- [chatlas](https://github.com/posit-dev/chatlas) - LLM integration library
- OpenAI GPT-4o-mini - Language model

## License

MIT License - feel free to use and modify as needed!

