import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from memory.hindsight_memory import recall_incidents
from agents.incident_matcher import build_historical_cases


def test_matcher():

    print("\n")
    print("=" * 75)
    print("BIOPROCESS INCIDENT COPILOT")
    print("HISTORICAL INCIDENT MATCHER TEST")
    print("=" * 75)

    query = """
    A microbial fermentation batch has a sudden
    dissolved oxygen decline at high biomass.
    Find historical incidents involving dissolved
    oxygen decline, oxygen limitation,
    interventions and recovery.
    """

    print("\nSearching Hindsight...")

    results = recall_incidents(query)

    memories = [
        result.text
        for result in results.results
    ]

    print(
        f"Hindsight returned "
        f"{len(memories)} memories."
    )

    print("\nBuilding historical incident cases...")

    cases = build_historical_cases(
        memories=memories,
        incident_type="dissolved oxygen decline"
    )

    print(
        f"\nHistorical cases identified: "
        f"{len(cases)}"
    )

    print("\n")
    print("=" * 75)
    print("RANKED HISTORICAL INCIDENTS")
    print("=" * 75)

    for index, case in enumerate(
        cases[:5],
        start=1
    ):

        print(
            f"\nCASE {index}: "
            f"{case['batch_id']}"
        )

        print(
            f"Relevance score: "
            f"{case['score']}"
        )

        print(
            f"Evidence count: "
            f"{len(case['evidence'])}"
        )

        print("\nEvidence:")

        for evidence in case["evidence"][:5]:

            print(
                f"  • {evidence}"
            )


if __name__ == "__main__":

    test_matcher()

    print("\n")
    print("=" * 75)
    print("INCIDENT MATCHER TEST COMPLETE")
    print("=" * 75)