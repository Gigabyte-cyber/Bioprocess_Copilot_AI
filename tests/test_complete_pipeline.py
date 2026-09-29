import sys
import os

# Add project root to Python path
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.insert(0, PROJECT_ROOT)

from agents.copilot import run_copilot


print("=" * 75)
print("BIOPROCESS INCIDENT COPILOT")
print("COMPLETE END-TO-END PIPELINE TEST")
print("=" * 75)


incident = {
    "batch_id": "B125",
    "process_stage": "Microbial fermentation",
    "dissolved_oxygen": 23.16,
    "previous_dissolved_oxygen": 47,
    "agitation": 260,
    "aeration": 1.5,
    "biomass": 19.5,
    "temperature": 37,
    "pH": 6.8
}


print("\nCURRENT INCIDENT")
print("-" * 75)

for key, value in incident.items():
    print(f"{key}: {value}")


print("\nRunning complete Bioprocess Incident Copilot...")
print("Hindsight -> Memory -> Incident Matching -> Evidence -> Groq")
print()


try:

    result = run_copilot(incident)

    print("\n")
    print("=" * 75)
    print("FINAL BIOPROCESS INCIDENT COPILOT REPORT")
    print("=" * 75)

    print(result)

    print("\n")
    print("=" * 75)
    print("COMPLETE PIPELINE TEST SUCCESSFUL")
    print("=" * 75)

finally:

    # Cleanly close Hindsight HTTP resources
    try:
        from memory.hindsight_memory import close_hindsight
        close_hindsight()
        print("\nHindsight client closed successfully.")
    except Exception as cleanup_error:
        print(
            f"\nHindsight cleanup warning: {cleanup_error}"
        )