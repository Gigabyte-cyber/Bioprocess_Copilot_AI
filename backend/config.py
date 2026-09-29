import os
from dotenv import load_dotenv

# Load variables from the project's .env file
load_dotenv()

# -----------------------------
# Groq
# -----------------------------

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "openai/gpt-oss-120b"
)

# -----------------------------
# Hindsight
# -----------------------------

HINDSIGHT_API_KEY = os.getenv("HINDSIGHT_API_KEY")

HINDSIGHT_API_URL = os.getenv(
    "HINDSIGHT_API_URL",
    "https://api.hindsight.vectorize.io"
)

HINDSIGHT_BANK_ID = os.getenv(
    "HINDSIGHT_BANK_ID",
    "bioprocess-incidents"
)


def validate_config():

    missing = []

    if not GROQ_API_KEY:
        missing.append("GROQ_API_KEY")

    if not HINDSIGHT_API_KEY:
        missing.append("HINDSIGHT_API_KEY")

    if missing:
        raise RuntimeError(
            "Missing environment variables: "
            + ", ".join(missing)
        )


if __name__ == "__main__":

    validate_config()

    print("Configuration loaded successfully.")
    print("Groq model:", GROQ_MODEL)
    print("Hindsight URL:", HINDSIGHT_API_URL)
    print("Hindsight bank:", HINDSIGHT_BANK_ID)