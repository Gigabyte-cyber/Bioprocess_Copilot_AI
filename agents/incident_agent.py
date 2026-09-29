from groq import Groq

from backend.config import (
    GROQ_API_KEY,
    GROQ_MODEL
)

from memory.hindsight_memory import recall_incidents

from agents.prompts import (
    SYSTEM_PROMPT,
    INCIDENT_ANALYSIS_PROMPT
)


# ==========================================
# Groq Client
# ==========================================

groq_client = Groq(
    api_key=GROQ_API_KEY
)


# ==========================================
# Historical Memory
# ==========================================

def retrieve_historical_memory(
    incident: str
) -> str:
    """
    Search Hindsight for incidents relevant
    to the current process incident.
    """

    results = recall_incidents(
        incident
    )

    if not results.results:
        return "No relevant historical incidents were found."

    memories = []

    for index, result in enumerate(
        results.results,
        start=1
    ):

        memories.append(
            f"Historical Memory {index}:\n"
            f"{result.text}"
        )

    return "\n\n".join(memories)


# ==========================================
# Incident Analysis
# ==========================================

def analyze_incident(
    current_incident: str
) -> dict:
    """
    Complete Bioprocess Incident Copilot workflow:

    Current Incident
          ↓
    Hindsight Recall
          ↓
    Groq Analysis
          ↓
    Incident Brief
    """

    # --------------------------------------
    # 1. Retrieve historical memory
    # --------------------------------------

    historical_memory = retrieve_historical_memory(
        current_incident
    )

    # --------------------------------------
    # 2. Build analysis prompt
    # --------------------------------------

    analysis_prompt = INCIDENT_ANALYSIS_PROMPT.format(
        current_incident=current_incident,
        historical_memory=historical_memory
    )

    # --------------------------------------
    # 3. Ask Groq to analyze
    # --------------------------------------

    response = groq_client.chat.completions.create(

        model=GROQ_MODEL,

        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": analysis_prompt
            }
        ],

        temperature=0.2
    )

    analysis = response.choices[0].message.content

    # --------------------------------------
    # 4. Return complete result
    # --------------------------------------

    return {
        "current_incident": current_incident,
        "historical_memory": historical_memory,
        "analysis": analysis
    }


# ==========================================
# Simple Groq Test
# ==========================================

def test_groq_connection():

    response = groq_client.chat.completions.create(

        model=GROQ_MODEL,

        messages=[
            {
                "role": "system",
                "content": (
                    "You are Bioprocess Copilot, "
                    "an AI assistant that helps "
                    "bioprocess engineers investigate "
                    "process incidents."
                )
            },
            {
                "role": "user",
                "content": (
                    "Explain in two sentences why "
                    "dissolved oxygen is important "
                    "during microbial fermentation."
                )
            }
        ]
    )

    return response.choices[0].message.content