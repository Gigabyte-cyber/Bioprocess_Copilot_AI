import sys
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from memory.hindsight_memory import recall_incidents


def search_memory(title, query):

    print("\n")
    print("=" * 75)
    print(title)
    print("=" * 75)

    print("\nQuery:")
    print(query)

    try:

        results = recall_incidents(query)

        print("\nRetrieved historical memories:")
        print("-" * 75)

        if not results.results:

            print("No memories found.")

            return

        for index, result in enumerate(
            results.results,
            start=1
        ):

            print(f"\nMemory {index}:")
            print(result.text)

    except Exception as error:

        print("\nSearch failed:")
        print(error)


# ==========================================================
# TEST 1 — Dissolved Oxygen
# ==========================================================

search_memory(
    "TEST 1 — DISSOLVED OXYGEN",
    """
    A microbial fermentation batch has a sudden
    dissolved oxygen decline at high biomass.
    Find historical incidents involving oxygen
    limitation, dissolved oxygen decline,
    interventions and recovery.
    """
)


# ==========================================================
# TEST 2 — pH
# ==========================================================

search_memory(
    "TEST 2 — pH",
    """
    A microbial fermentation batch is experiencing
    abnormal pH drift. Find historical incidents
    involving pH deviations and previous corrective
    actions.
    """
)


# ==========================================================
# TEST 3 — Temperature
# ==========================================================

search_memory(
    "TEST 3 — TEMPERATURE",
    """
    A fermentation batch is experiencing an unexpected
    temperature increase. Find historical incidents
    involving temperature deviations and previous
    interventions.
    """
)


print("\n")
print("=" * 75)
print("MEMORY SEARCH TEST COMPLETE")
print("=" * 75)