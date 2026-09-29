import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is missing from .env")

client = Groq(api_key=GROQ_API_KEY)


SYSTEM_PROMPT = """
You are the Bioprocess Incident Copilot.

You are an AI decision-support assistant for bioprocess and
fermentation engineers.

Your job is to analyze a CURRENT PROCESS INCIDENT using
HISTORICAL EVIDENCE retrieved from Hindsight memory.

IMPORTANT RULES:

1. Use the supplied historical evidence as the primary evidence base.
2. Do not invent historical incidents, measurements, outcomes,
   interventions, or causes.
3. Clearly distinguish historical facts from interpretation.
4. Do not claim certainty when the evidence is limited.
5. Do not automatically instruct an operator to change a process.
6. Present interventions from historical incidents as historical
   evidence, not as guaranteed solutions for the current batch.
7. Recommend verification checks before process intervention.
8. If evidence is insufficient, explicitly say so.
9. Keep the answer practical and understandable to a bioprocess engineer.

Return the analysis using exactly these sections:

INCIDENT SUMMARY

CURRENT PROCESS CONDITIONS

HISTORICAL MATCHES

HISTORICAL EVIDENCE

POSSIBLE INTERPRETATION

HISTORICAL INTERVENTIONS

HISTORICAL OUTCOMES

RECOMMENDED VERIFICATION CHECKS

CONFIDENCE

EVIDENCE LIMITATIONS

The final response should be concise but technically useful.
"""


def build_prompt(current_incident, evidence_package):
    return f"""
Analyze the following current bioprocess incident.

================ CURRENT INCIDENT ================

{current_incident}

================ HISTORICAL EVIDENCE ================

{evidence_package}

================ TASK ================

Compare the current incident with the historical evidence.

Identify the most relevant historical incidents.

Explain what happened historically.

Explain which interventions were used historically.

Explain the historical outcomes.

Provide possible interpretations for the current incident,
but clearly label them as interpretations rather than confirmed causes.

Provide verification checks that should be considered before
any process intervention.

Do not invent evidence that is not present in the supplied data.
"""


def analyze_incident(current_incident, evidence_package):

    prompt = build_prompt(
        current_incident,
        evidence_package
    )

    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=2500
    )

    return response.choices[0].message.content


def test_final_agent():

    current_incident = """
Batch ID: B120

Process stage: Microbial fermentation

Dissolved oxygen: 23%
Previous dissolved oxygen: 47%

Agitation: 260 RPM
Aeration: 1.5 vvm
Biomass: 19.5 g/L
Temperature: 37°C
pH: 6.8

The dissolved oxygen level has decreased rapidly.
"""

    evidence_package = """
HISTORICAL CASE 1

Batch: B081
Relevance score: 54

Evidence:
- Batch B081 experienced a dissolved oxygen decline
  from 46% to 25%.
- Process team increased agitation.
- Dissolved oxygen recovered to 41% within approximately
  13 minutes.


HISTORICAL CASE 2

Batch: B047
Relevance score: 48

Evidence:
- Batch B047 experienced a dissolved oxygen decline
  from 45% to 24%.
- Oxygen demand increased as biomass concentration rose.
- Agitation increased from 250 RPM to 320 RPM.
- Dissolved oxygen recovered from 24% to 39%
  over approximately 11 minutes.
"""

    print("=" * 75)
    print("BIOPROCESS INCIDENT COPILOT")
    print("FINAL GROQ REASONING TEST")
    print("=" * 75)

    print("\nAnalyzing current incident...")
    print("Using historical evidence from Hindsight...")
    print("Sending grounded evidence to Groq...")

    result = analyze_incident(
        current_incident,
        evidence_package
    )

    print("\n")
    print("=" * 75)
    print("BIOPROCESS INCIDENT BRIEF")
    print("=" * 75)

    print(result)

    print("\n")
    print("=" * 75)
    print("FINAL AGENT TEST COMPLETE")
    print("=" * 75)


if __name__ == "__main__":
    test_final_agent()