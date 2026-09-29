import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from memory.hindsight_memory import recall_incidents

from agents.incident_matcher import (
    build_historical_cases
)

from agents.evidence_builder import (
    build_evidence_package
)


def main():

    print("\n")
    print("=" * 75)
    print("BIOPROCESS INCIDENT COPILOT")
    print("EVIDENCE PACKAGE TEST")
    print("=" * 75)

    # --------------------------------------------------
    # Current incident
    # --------------------------------------------------

    current_incident = {

        "batch_id": "B120",

        "process_stage":
            "Microbial fermentation",

        "dissolved_oxygen": 23,

        "previous_dissolved_oxygen": 47,

        "agitation": 260,

        "aeration": 1.5,

        "biomass": 19.5,

        "temperature": 37,

        "pH": 6.8
    }

    print("\nCURRENT INCIDENT")
    print("-" * 75)

    for key, value in current_incident.items():

        print(
            f"{key}: {value}"
        )

    # --------------------------------------------------
    # Hindsight search
    # --------------------------------------------------

    query = """
    A microbial fermentation batch has a sudden
    dissolved oxygen decline at high biomass.
    Find historical incidents involving dissolved
    oxygen decline, oxygen limitation,
    interventions and recovery.
    """

    print("\n")
    print("Searching Hindsight...")

    results = recall_incidents(query)

    memories = [
        result.text
        for result in results.results
    ]

    print(
        f"Hindsight returned "
        f"{len(memories)} memories."
    )

    # --------------------------------------------------
    # Incident matching
    # --------------------------------------------------

    historical_cases = build_historical_cases(
        memories=memories,

        incident_type=
            "dissolved oxygen decline"
    )

    print(
        f"Historical cases identified: "
        f"{len(historical_cases)}"
    )

    # --------------------------------------------------
    # Evidence package
    # --------------------------------------------------

    evidence_package = build_evidence_package(
        current_incident=
            current_incident,

        historical_cases=
            historical_cases,

        max_cases=3
    )

    print("\n")
    print("=" * 75)
    print("STRUCTURED HISTORICAL EVIDENCE")
    print("=" * 75)

    for index, case in enumerate(
        evidence_package["historical_cases"],
        start=1
    ):

        print(
            f"\nHISTORICAL CASE {index}"
        )

        print(
            f"Batch: {case['batch_id']}"
        )

        print(
            f"Relevance score: "
            f"{case['relevance_score']}"
        )

        print("\nEvidence:")

        for evidence in case["evidence"]:

            print(
                f"  • {evidence}"
            )

    print("\n")
    print("=" * 75)
    print("EVIDENCE PACKAGE READY FOR GROQ")
    print("=" * 75)


if __name__ == "__main__":

    main()