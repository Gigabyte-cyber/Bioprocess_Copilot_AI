import sys
from pathlib import Path

# Add the project root to Python's import path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from agents.incident_agent import test_groq_connection


print("=" * 60)
print("BIOPROCESS INCIDENT COPILOT")
print("GROQ AI CONNECTION TEST")
print("=" * 60)

try:

    answer = test_groq_connection()

    print("\nGroq response:")
    print("-" * 60)
    print(answer)
    print("-" * 60)

    print("\nGroq connection successful.")

except Exception as error:

    print("\nGroq connection failed.")
    print("\nError:")
    print(error)