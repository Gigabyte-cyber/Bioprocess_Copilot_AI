import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from memory.hindsight_memory import recall_incidents

from agents.evidence_selector import (
    select_relevant_memories
)


def run_test(title, query, incident_type, parameter):

    print("\n")
    print("=" * 75)
    print(title)
    print("=" * 75)

    # -----------------------------------------
    # Hindsight retrieval
    # -----------------------------------------

    results = recall_incidents(query)

    raw_memories = [
        result.text
        for result in results.results
    ]

    print(
        f"\nHindsight returned "
        f"{len(raw_memories)} memories."
    )

    # -----------------------------------------
    # Evidence selection
    # -----------------------------------------

    selected = select_relevant_memories(
        memories=raw_memories,
        incident_type=incident_type,
        parameter=parameter,
        max_memories=8
    )

    print(
        f"Evidence selector retained "
        f"{len(selected)} memories."
    )

    print("\nSELECTED HISTORICAL EVIDENCE")
    print("-" * 75)

    for index, memory in enumerate(
        selected,
        start=1
    ):

        print(f"\nEvidence {index}")
        print(memory)


# ==========================================================
# TEST 1 — DO
# ==========================================================

run_test(
    "EVIDENCE TEST 1 — DISSOLVED OXYGEN",

    """
    A microbial fermentation batch has a sudden
    dissolved oxygen decline at high biomass.
    Find historical incidents involving oxygen
    limitation, dissolved oxygen decline,
    interventions and recovery.
    """,

    "dissolved oxygen decline",

    "DO"
)


# ==========================================================
# TEST 2 — pH
# ==========================================================

run_test(
    "EVIDENCE TEST 2 — pH",

    """
    A microbial fermentation batch is experiencing
    abnormal pH drift. Find historical incidents
    involving pH deviations and corrective actions.
    """,

    "pH drift",

    "pH"
)


# ==========================================================
# TEST 3 — Temperature
# ==========================================================

run_test(
    "EVIDENCE TEST 3 — TEMPERATURE",

    """
    A fermentation batch is experiencing an unexpected
    temperature increase. Find historical incidents
    involving temperature deviations and interventions.
    """,

    "temperature rise",

    "temperature"
)


print("\n")
print("=" * 75)
print("EVIDENCE SELECTION TEST COMPLETE")
print("=" * 75)