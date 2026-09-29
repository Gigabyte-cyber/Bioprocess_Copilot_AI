import sys
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from memory.hindsight_memory import (
    remember_incident,
    recall_incidents
)


print("=" * 70)
print("BIOPROCESS INCIDENT COPILOT")
print("HINDSIGHT MEMORY TEST")
print("=" * 70)


# --------------------------------------------------
# Historical incident
# --------------------------------------------------

historical_incident = """
Batch ID: B047

Process stage:
Microbial fermentation

Incident:
Dissolved oxygen dropped unexpectedly from 45% to 24%.

Process conditions at the time:
- Agitation: 250 RPM
- Aeration: 1.5 vvm
- Biomass: 18.2 g/L
- Temperature: 37°C
- pH: 6.8

Investigation:
The process team observed that oxygen demand had increased
as biomass concentration increased.

Intervention:
Agitation was increased from 250 RPM to 320 RPM.

Outcome:
Dissolved oxygen recovered from 24% to 39%
within approximately 11 minutes.

Resolution:
The intervention successfully restored the dissolved
oxygen level.
"""


print("\n[1] Storing historical incident...")

try:

    result = remember_incident(
        incident_text=historical_incident,
        context="Historical bioprocess incident: Batch B047"
    )

    print("Historical incident stored successfully.")

except Exception as error:

    print("\nHindsight RETAIN failed.")
    print(error)
    raise SystemExit


# --------------------------------------------------
# Recall
# --------------------------------------------------

query = """
A fermentation batch is experiencing a sudden decrease
in dissolved oxygen. The biomass concentration is high,
and the engineer wants to know whether a similar incident
has happened previously and what intervention was successful.
"""


print("\n[2] Searching historical memory...")

try:

    results = recall_incidents(query)

    print("\nHINDSIGHT RECALL RESULTS")
    print("=" * 70)

    if not results.results:

        print("No historical incidents were returned.")

    else:

        for index, result in enumerate(results.results, start=1):

            print(f"\nMemory {index}")
            print("-" * 70)
            print(result.text)

except Exception as error:

    print("\nHindsight RECALL failed.")
    print(error)
    raise SystemExit


print("\n" + "=" * 70)
print("HINDSIGHT MEMORY TEST COMPLETE")
print("=" * 70)