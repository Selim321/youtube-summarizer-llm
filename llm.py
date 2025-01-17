from ollama import chat
from ollama import ChatResponse



def summarize_with_ollama(text, model="llama3.2"):
    
    prompt = f"""Please provide a concise summary of the following video transcript. 
    Focus on the main points and key takeaways:

    {text}

    Please structure the summary with:
    1. Main Topic
    2. Key Points
    3. Conclusion"""

    response: ChatResponse = chat(model=model, messages=[
  {
    'role': 'user',
    'content': prompt,
  },
])
    return response
