# 🧬 Bioprocess Incident Copilot AI

## AI-Powered Historical Incident Analysis for Bioprocessing

Bioprocess Incident Copilot AI is an AI-powered decision-support system designed to help bioprocess and fermentation engineers investigate process incidents using historical process knowledge.

The system combines:

- Hindsight historical memory
- Incident matching
- Evidence selection
- Evidence-grounded AI reasoning
- Groq LLM
- Streamlit interactive dashboard

---

## 🎯 Problem

Bioprocess engineers may encounter incidents such as:

- Dissolved oxygen decline
- Abnormal biomass behavior
- Temperature deviations
- pH deviations
- Oxygen-transfer limitations
- Process instability

Historical batch information can contain valuable evidence about how similar incidents occurred and what happened afterward.

However, manually searching historical records can be slow and difficult.

---

## 💡 Proposed Solution

Bioprocess Incident Copilot AI retrieves relevant historical incidents and provides an evidence-grounded analysis of the current process condition.

The system does not rely only on general AI knowledge.

Instead, it follows the workflow:

Current Incident
        ↓
Hindsight Historical Memory
        ↓
Incident Matching
        ↓
Evidence Selection
        ↓
Evidence Package
        ↓
Groq Reasoning
        ↓
Bioprocess Incident Report

---

## 🧠 System Architecture

### 1. Current Incident

The user enters process information such as:

- Batch ID
- Process stage
- Dissolved oxygen
- Previous dissolved oxygen
- Agitation
- Aeration
- Biomass
- Temperature
- pH

### 2. Historical Memory

Hindsight stores historical bioprocess incidents.

The system retrieves memories relevant to the current incident.

### 3. Incident Matching

Historical memories are grouped into historical batch cases and ranked according to relevance.

### 4. Evidence Builder

The most relevant historical cases are selected and converted into a structured evidence package.

### 5. AI Reasoning

Groq analyzes the current incident using the retrieved historical evidence.

The AI is instructed not to invent historical measurements or interventions.

### 6. Final Report

The system produces:

- Incident Summary
- Current Process Conditions
- Historical Matches
- Historical Evidence
- Possible Interpretation
- Historical Interventions
- Historical Outcomes
- Recommended Verification Checks
- Confidence
- Evidence Limitations

---

## 🧪 Example Incident

Batch:

B125

Process:

Microbial fermentation

Dissolved oxygen:

23.16%

Previous dissolved oxygen:

47%

Agitation:

260 RPM

Aeration:

1.5 vvm

Biomass:

19.5 g/L

Temperature:

37°C

pH:

6.8

The system identifies historical cases such as B081 and B047 involving comparable dissolved oxygen declines.

Historical evidence is then provided to the reasoning model before generating the incident report.

---

## 🛠️ Technologies

- Python
- Streamlit
- Groq
- Hindsight
- FastAPI
- Python-dotenv

---

## 📁 Project Structure

agents/
    copilot.py
    evidence_builder.py
    evidence_selector.py
    final_agent.py
    incident_agent.py
    incident_matcher.py
    prompts.py

backend/
    config.py
    main.py
    schemas.py

memory/
    hindsight_memory.py

tools/
    incident_analysis.py
    load_incidents.py
    process_analysis.py

tests/
    test_agent.py
    test_complete_pipeline.py
    test_evidence_builder.py
    test_evidence_selector.py
    test_final_agent.py
    test_groq.py
    test_hindsight.py
    test_incident_matcher.py
    test_learning.py
    test_memory_search.py

app.py

---

## 🚀 Running the Application

Activate the virtual environment:

```powershell
.venv\Scripts\Activate.ps1