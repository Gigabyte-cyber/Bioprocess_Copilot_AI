from typing import List, Dict


def select_relevant_memories(
    memories: List[str],
    incident_type: str,
    parameter: str,
    max_memories: int = 8
) -> List[str]:
    """
    Select the most relevant Hindsight memories
    using simple transparent keyword matching.

    This is an evidence-filtering layer before
    memories are passed to the LLM.
    """

    incident_type = incident_type.lower()
    parameter = parameter.lower()

    scored_memories = []

    for memory in memories:

        text = memory.lower()

        score = 0

        # -----------------------------------------
        # Incident type match
        # -----------------------------------------

        incident_words = incident_type.split()

        for word in incident_words:

            if len(word) > 2 and word in text:
                score += 3

        # -----------------------------------------
        # Parameter match
        # -----------------------------------------

        parameter_words = parameter.split()

        for word in parameter_words:

            if len(word) > 2 and word in text:
                score += 4

        # -----------------------------------------
        # Useful historical evidence
        # -----------------------------------------

        evidence_terms = [
            "intervention",
            "resolved",
            "recovered",
            "outcome",
            "response",
            "corrected",
            "returned",
            "improved"
        ]

        for term in evidence_terms:

            if term in text:
                score += 1

        # -----------------------------------------
        # Keep scored result
        # -----------------------------------------

        if score > 0:

            scored_memories.append(
                {
                    "score": score,
                    "memory": memory
                }
            )

    # -----------------------------------------
    # Sort by relevance
    # -----------------------------------------

    scored_memories.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    # -----------------------------------------
    # Return top results
    # -----------------------------------------

    return [
        item["memory"]
        for item in scored_memories[:max_memories]
    ]