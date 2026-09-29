import streamlit as st
import sys
import os

# Add project root to Python path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from agents.copilot import run_copilot


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Bioprocess Incident Copilot",
    page_icon="🧬",
    layout="wide"
)


# ============================================================
# HEADER
# ============================================================

st.title("🧬 Bioprocess Incident Copilot")

st.markdown(
    """
    ### AI-Powered Historical Incident Analysis

    Analyze a current fermentation incident using historical
    process evidence retrieved from Hindsight and grounded
    reasoning through Groq.
    """
)

st.divider()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header("⚙️ Process Configuration")

batch_id = st.sidebar.text_input(
    "Batch ID",
    value="B120"
)

process_stage = st.sidebar.text_input(
    "Process Stage",
    value="Microbial fermentation"
)

st.sidebar.subheader("Process Parameters")

dissolved_oxygen = st.sidebar.number_input(
    "Current Dissolved Oxygen (%)",
    value=23.0
)

previous_dissolved_oxygen = st.sidebar.number_input(
    "Previous Dissolved Oxygen (%)",
    value=47.0
)

agitation = st.sidebar.number_input(
    "Agitation (RPM)",
    value=260.0
)

aeration = st.sidebar.number_input(
    "Aeration (vvm)",
    value=1.5
)

biomass = st.sidebar.number_input(
    "Biomass (g/L)",
    value=19.5
)

temperature = st.sidebar.number_input(
    "Temperature (°C)",
    value=37.0
)

ph = st.sidebar.number_input(
    "pH",
    value=6.8
)


# ============================================================
# CURRENT CONDITIONS
# ============================================================

st.header("📊 Current Process Conditions")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Dissolved Oxygen",
    f"{dissolved_oxygen:.1f} %",
    f"{dissolved_oxygen - previous_dissolved_oxygen:.1f} %"
)

col2.metric(
    "Agitation",
    f"{agitation:.0f} RPM"
)

col3.metric(
    "Aeration",
    f"{aeration:.1f} vvm"
)

col4.metric(
    "Biomass",
    f"{biomass:.1f} g/L"
)


col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Temperature",
    f"{temperature:.1f} °C"
)

col2.metric(
    "pH",
    f"{ph:.2f}"
)

col3.metric(
    "Batch",
    batch_id
)

col4.metric(
    "Process Stage",
    process_stage
)


st.divider()


# ============================================================
# INCIDENT ANALYSIS
# ============================================================

st.header("🔬 Incident Analysis")

analyze_button = st.button(
    "🚀 Analyze Incident",
    type="primary",
    use_container_width=True
)


if analyze_button:

    incident = {
        "batch_id": batch_id,
        "process_stage": process_stage,
        "dissolved_oxygen": dissolved_oxygen,
        "previous_dissolved_oxygen": previous_dissolved_oxygen,
        "agitation": agitation,
        "aeration": aeration,
        "biomass": biomass,
        "temperature": temperature,
        "pH": ph
    }

    with st.spinner(
        "Searching historical memory and analyzing incident..."
    ):

        try:

            result = run_copilot(incident)

            st.success(
                "Incident analysis completed successfully."
            )

            st.divider()

            st.header("📋 Bioprocess Incident Report")

            st.markdown(result)

        except Exception as e:

            st.error(
                f"Analysis failed: {e}"
            )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Bioprocess Incident Copilot • Hindsight Historical Memory • "
    "Evidence-Grounded Groq Reasoning"
)