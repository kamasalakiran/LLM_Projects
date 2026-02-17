from groq import Groq
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()

client = Groq()

def summarize(text):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a text summarizer. Summarize the given text in 3-5 bullet points."},
            {"role": "user", "content": f"Summarize this:\n\n{text}"}
        ]
    )
    return response.choices[0].message.content

# Test text
sample_text = """
Artificial intelligence is transforming industries across the globe. 
From healthcare to finance, AI systems are being used to automate tasks, 
improve decision-making, and create new products and services. 
Machine learning, a subset of AI, allows systems to learn from data 
without being explicitly programmed. Deep learning, a further subset, 
uses neural networks with many layers to analyze various factors of data. 
Natural language processing allows machines to understand human language, 
while computer vision enables machines to interpret visual information.
"""

print("Summarizing...\n")
result = summarize(sample_text)
print(result)