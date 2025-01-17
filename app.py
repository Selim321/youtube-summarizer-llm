import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import requests
from urllib.parse import urlparse, parse_qs
from llm import summarize_with_ollama

def extract_video_id(url):
    """Extract video ID from YouTube URL."""
    parsed_url = urlparse(url)
    if parsed_url.hostname == 'youtu.be':
        return parsed_url.path[1:]
    if parsed_url.hostname in ('www.youtube.com', 'youtube.com'):
        if parsed_url.path == '/watch':
            return parse_qs(parsed_url.query)['v'][0]
    return None

def get_transcript(video_id):
    """Get transcript of YouTube video."""
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ' '.join([t['text'] for t in transcript_list])
        return transcript
    except Exception as e:
        st.error(f"Error fetching transcript: {str(e)}")
        return None


# Streamlit UI
st.set_page_config(page_title="YouTube Video Summarizer", page_icon="📺")
st.title("YouTube Video Summarizer")

# Input section
st.markdown("### Enter YouTube Video URL")
video_url = st.text_input("", placeholder="https://www.youtube.com/watch?v=...")

# Model selection
model_option = st.selectbox(
    "Select Ollama Model",
    ["llama3.2", "mistral", "gemma", "neural-chat"],
    index=0
)

if st.button("Summarize"):
    if video_url:
        with st.spinner("Processing video..."):
            # Extract video ID
            video_id = extract_video_id(video_url)
            
            if not video_id:
                st.error("Invalid YouTube URL. Please check the URL and try again.")
            else:
                # Get transcript
                transcript = get_transcript(video_id)
                
                if transcript:
                    st.info("Generating summary...")
                    
                    # Get summary
                    summary = summarize_with_ollama(transcript, model_option)
                    
                    # Display results
                    st.markdown("### Summary")
                    st.write(summary["message"]["content"])
                    
                    # Display original transcript in expander
                    with st.expander("Show Original Transcript"):
                        st.write(transcript)
    else:
        st.warning("Please enter a YouTube URL")

# Add footer with instructions
st.markdown("---")
st.markdown("""
### How to use:
1. Make sure Ollama is running locally with your chosen model
2. Paste a YouTube video URL
3. Select your preferred Ollama model
4. Click 'Summarize' to generate the summary
""")