from datetime import datetime

from memory.hindsight_memory import remember_incident


def record_incident_outcome(
    batch_id: str,
    incident: str,
    intervention: str,
    outcome: str,
    engineer_notes: str = ""
):
    """
    Record the final outcome of an incident so that
    future incidents can benefit from the experience.
    """

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    memory = f"""
BIOPROCESS INCIDENT OUTCOME

Date:
{timestamp}

Batch ID:
{batch_id}

Original Incident:
{incident}

Intervention:
{intervention}

Outcome:
{outcome}

Engineer Notes:
{engineer_notes}

This incident has been resolved and recorded as
historical process experience for future incident
investigation.
"""

    return remember_incident(
        incident_text=memory,
        context="Resolved bioprocess incident outcome"
    )