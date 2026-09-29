import sys
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


from agents.incident_agent import analyze_incident


print("=" * 75)
print("BIOPROCESS INCIDENT COPILOT")
print("FIRST COMPLETE AGENT TEST")
print("=" * 75)


# ==========================================
# NEW INCIDENT
# ==========================================

current_incident = """
Batch ID: B081

Process stage:
Microbial fermentation

Current observations:

- Dissolved oxygen: 25%
- Previous dissolved oxygen: 46%
- Agitation: 255 RPM
- Aeration: 1.5 vvm
- Biomass: 18.8 g/L
- Temperature: 37°C
- pH: 6.8

The dissolved oxygen level has dropped rapidly
during the fermentation process.

The engineer wants to know whether a similar
incident occurred previously and what happened
during that historical event.
"""


print("\nCURRENT INCIDENT")
print("=" * 75)
print(current_incident)


# ==========================================
# RUN COPILOT
# ==========================================

print("\nRunning Bioprocess Incident Copilot...")
print("Searching Hindsight memory...")
print("Analyzing with Groq...")


try:

    result = analyze_incident(
        current_incident
    )

except Exception as error:

    print("\nAgent failed.")
    print(error)
    raise SystemExit


# ==========================================
# DISPLAY MEMORY
# ==========================================

print("\n")
print("=" * 75)
print("HISTORICAL MEMORY RETRIEVED")
print("=" * 75)

print(
    result["historical_memory"]
)


# ==========================================
# DISPLAY AI ANALYSIS
# ==========================================

print("\n")
print("=" * 75)
print("BIOPROCESS INCIDENT BRIEF")
print("=" * 75)

print(
    result["analysis"]
)


print("\n")
print("=" * 75)
print("COPILOT TEST COMPLETE")
print("=" * 75)