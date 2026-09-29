from typing import List, Dict


def build_historical_cases(
    memories: List[str],
    incident_type: str
) -> List[Dict]:
    """
    Convert raw Hindsight memories into grouped
    historical incident cases.

    The function groups memories by batch ID.
    """

    cases = {}

    incident_type = incident_type.lower()

    for memory in memories:

        text = memory.lower()

        # -----------------------------------------
        # Identify batch ID
        # -----------------------------------------

        batch_id = None

        words = memory.replace(",", " ").split()

        for word in words:

            cleaned = (
                word
                .replace(".", "")
                .replace(":", "")
                .replace(";", "")
            )

            if (
                cleaned.startswith("B")
                and len(cleaned) == 4
                and cleaned[1:].isdigit()
            ):
                batch_id = cleaned
                break

        if not batch_id:
            continue

        # -----------------------------------------
        # Calculate relevance
        # -----------------------------------------

        score = 0

        incident_words = incident_type.split()

        for word in incident_words:

            if len(word) > 2 and word in text:
                score += 4

        # -----------------------------------------
        # Evidence terms
        # -----------------------------------------

        evidence_terms = [
            "resolved",
            "recovered",
            "intervention",
            "increased",
            "decreased",
            "corrected",
            "returned",
            "restored",
            "improved"
        ]

        for term in evidence_terms:

            if term in text:
                score += 1

        # -----------------------------------------
        # Create case
        # -----------------------------------------

        if batch_id not in cases:

            cases[batch_id] = {
                "batch_id": batch_id,
                "score": 0,
                "evidence": []
            }

        cases[batch_id]["score"] += score
        cases[batch_id]["evidence"].append(memory)

    # -----------------------------------------
    # Sort cases
    # -----------------------------------------

    ranked_cases = sorted(
        cases.values(),
        key=lambda case: case["score"],
        reverse=True
    )

    return ranked_cases