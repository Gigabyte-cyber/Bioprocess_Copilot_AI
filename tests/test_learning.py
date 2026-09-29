import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from tools.incident_analysis import (
    record_incident_outcome
)

from memory.hindsight_memory import (
    recall_incidents
)


print("=" * 75)
print("BIOPROCESS INCIDENT COPILOT")
print("CONTINUOUS LEARNING TEST")
print("=" * 75)


# ==========================================================
# Record the outcome of the current incident
# ==========================================================

batch_id = "B081"

incident = """
Dissolved oxygen dropped from 46% to 25%
during microbial fermentation.

Biomass was 18.8 g/L.
Agitation was 255 RPM.
Aeration was 1.5 vvm.
"""


intervention = """
The process team increased agitation while
monitoring dissolved oxygen response.
"""


outcome = """
Dissolved oxygen recovered to 41% within
approximately 13 minutes.

No further abnormal oxygen decline was observed
during the monitored period.
"""


engineer_notes = """
The response was similar to the historical B047
incident. The process team will continue monitoring
oxygen demand as biomass increases.
"""


print("\n[1] Recording resolved incident...")

try:

    record_incident_outcome(
        batch_id=batch_id,
        incident=incident,
        intervention=intervention,
        outcome=outcome,
        engineer_notes=engineer_notes
    )

    print("Incident outcome successfully stored.")

except Exception as error:

    print("Failed to store incident outcome.")
    print(error)
    raise SystemExit


# ==========================================================
# Test future recall
# ==========================================================

print("\n[2] Searching memory for similar oxygen incidents...")


query = """
A future microbial fermentation batch has a sudden
dissolved oxygen decrease at high biomass concentration.
Find previous incidents, interventions and outcomes
that may be relevant.
"""


try:

    results = recall_incidents(query)

    print("\nHISTORICAL EXPERIENCE AVAILABLE TO FUTURE AGENTS")
    print("=" * 75)

    for index, result in enumerate(
        results.results,
        start=1
    ):

        print(f"\nMemory {index}")
        print("-" * 75)
        print(result.text)


except Exception as error:

    print("Memory recall failed.")
    print(error)
    raise SystemExit


print("\n")
print("=" * 75)
print("CONTINUOUS LEARNING TEST COMPLETE")
print("=" * 75)