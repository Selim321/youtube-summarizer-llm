# YouTube Video Summarizer

A Streamlit application that generates summaries of YouTube videos using the power of Large Language Models through Ollama. The app extracts transcripts from YouTube videos and processes them to create concise, structured summaries.

## Features

- Extract transcripts from YouTube videos using just the URL
- Process transcripts using various Ollama models (llama2, mistral, gemma, neural-chat)
- Generate structured summaries with main topics, key points, and conclusions
- View original transcripts alongside summaries
- User-friendly Streamlit interface

## Prerequisites

- Python 3.8+
- Ollama installed and running locally
- Internet connection for accessing YouTube transcripts

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd youtube-summarizer
```

2. Install the required dependencies:
```bash
pip install streamlit youtube-transcript-api requests
```

3. Make sure Ollama is installed and running with your preferred models:
```bash
# Install Ollama from: https://ollama.ai/
# Pull your preferred model, for example:
ollama pull llama2
```

## Usage

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided local URL (typically `http://localhost:8501`)

3. Enter a YouTube URL in the input field

4. Select your preferred Ollama model from the dropdown menu

5. Click "Summarize" to generate the video summary

## How It Works

1. The application takes a YouTube video URL as input
2. Extracts the video transcript using the `youtube_transcript_api`
3. Processes the transcript using the selected Ollama model
4. Generates a structured summary with main topics, key points, and conclusions
5. Displays both the summary and the original transcript

## Limitations

- Only works with YouTube videos that have available transcripts
- Requires Ollama to be running locally
- Processing time depends on the length of the video and the chosen model
- Some videos might have transcripts disabled by content creators

## Acknowledgments

- [Streamlit](https://streamlit.io/) for the web interface
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api) for transcript extraction
- [Ollama](https://ollama.ai/) for local LLM processing