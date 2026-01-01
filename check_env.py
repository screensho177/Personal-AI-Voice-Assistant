import os
from dotenv import load_dotenv

load_dotenv()

print("GROQ_API_KEY:", os.getenv("GROQ_API_KEY"))
print("DEEPGRAM_API_KEY:", os.getenv("DEEPGRAM_API_KEY"))
print("TAVILY_API_KEY:", os.getenv("TAVILY_API_KEY"))