from typing import List, Dict


def build_evidence_package(
    current_incident: Dict,
    historical_cases: List[Dict],
    max_cases: int = 3
) -> Dict:
    """
    Build a structured evidence package that can be
    passed to the LLM for incident analysis.
    """

    selected_cases = historical_cases[:max_cases]

    package = {
        "current_incident": current_incident,
        "historical_cases": []
    }

    for case in selected_cases:

        historical_case = {
            "batch_id": case["batch_id"],
            "relevance_score": case["score"],
            "evidence": case["evidence"]
        }

        package["historical_cases"].append(
            historical_case
        )

    return package