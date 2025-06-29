# Liova

Liova is a Flask web application for refactoring emails using the OpenAI API. Users can create accounts, log in, and rewrite emails with a simple interface. The app displays a diff between the original and refactored email.

## Setup

1. Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Set your OpenAI API key in the environment:

```bash
export OPENAI_API_KEY=your-key
```

3. Run the application:

```bash
python app.py
```

The app will start on `http://localhost:5000`.
