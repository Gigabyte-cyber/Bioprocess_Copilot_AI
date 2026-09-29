from hindsight_client import Hindsight

from backend.config import (
    HINDSIGHT_API_KEY,
    HINDSIGHT_API_URL,
    HINDSIGHT_BANK_ID
)


# ==========================================
# Hindsight Client
# ==========================================

hindsight_client = Hindsight(
    base_url=HINDSIGHT_API_URL,
    api_key=HINDSIGHT_API_KEY
)


def get_hindsight_client():
    """Return the Hindsight client."""
    return hindsight_client


def get_bank_id():
    """Return the project memory bank."""
    return HINDSIGHT_BANK_ID


def remember_incident(
    incident_text: str,
    context: str = "Bioprocess incident"
):
    """Store a bioprocess incident in Hindsight."""

    return hindsight_client.retain(
        bank_id=HINDSIGHT_BANK_ID,
        content=incident_text,
        context=context
    )


def recall_incidents(query: str):
    """Search Hindsight for relevant historical incidents."""

    return hindsight_client.recall(
        bank_id=HINDSIGHT_BANK_ID,
        query=query
    )


def close_hindsight():
    """Close the Hindsight HTTP client cleanly."""

    try:
        hindsight_client.close()
    except Exception:
        pass