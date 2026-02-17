from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()

def explain_code(code):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a code explainer. Explain the given code in simple plain English that a beginner can understand. Break it down line by line if needed."},
            {"role": "user", "content": f"Explain this code:\n\n{code}"}
        ]
    )
    return response.choices[0].message.content

# Test code
sample_code = """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(10)
print(result)
"""

print("Explaining code...\n")
result = explain_code(sample_code)
print(result)