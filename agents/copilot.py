from agents.evidence_builder import build_evidence_package
from agents.final_agent import analyze_incident
from memory.hindsight_memory import recall_incidents, close_hindsight
from agents.incident_matcher import build_historical_cases


def run_copilot(incident):

    print("[1/4] Searching Hindsight historical memory...")

    # Convert incident dictionary into a searchable query
    incident_query = (
        f"{incident.get('process_stage', '')} "
        f"dissolved oxygen "
        f"{incident.get('dissolved_oxygen', '')} "
        f"{incident.get('previous_dissolved_oxygen', '')} "
        f"agitation {incident.get('agitation', '')} "
        f"aeration {incident.get('aeration', '')}"
    )

    results = recall_incidents(incident_query)

    memories = []

    if results and results.results:
        memories = [
            result.text
            for result in results.results
        ]

    print(f"      Hindsight returned {len(memories)} memories.")

    print("[2/4] Matching current incident with historical cases...")

    historical_cases = build_historical_cases(
        memories,
        "dissolved oxygen"
    )

    print(
        f"      Identified {len(historical_cases)} "
        f"historical incident cases."
    )

    print("[3/4] Building evidence package...")

    evidence_package = build_evidence_package(
        incident,
        historical_cases,
        max_cases=3
    )

    print(
        f"      Selected "
        f"{len(evidence_package['historical_cases'])} "
        f"historical cases."
    )

    print("[4/4] Sending grounded evidence to Groq...")

    result = analyze_incident(
        incident,
        evidence_package
    )

    return result