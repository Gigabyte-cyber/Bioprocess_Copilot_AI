import sys
from pathlib import Path

import pandas as pd

# ---------------------------------------------------------
# Add project root to Python path
# ---------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from memory.hindsight_memory import remember_incident


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

DATA_FILE = PROJECT_ROOT / "data" / "incidents.csv"


# ---------------------------------------------------------
# Convert one CSV row into a detailed memory
# ---------------------------------------------------------

def create_incident_memory(row):

    return f"""
HISTORICAL BIOPROCESS INCIDENT

Batch ID:
{row['batch_id']}

Process Stage:
{row['process_stage']}

Incident Type:
{row['incident_type']}

Affected Parameter:
{row['parameter']}

Previous Value:
{row['previous_value']}

Incident Value:
{row['current_value']}

Agitation:
{row['agitation_rpm']} RPM

Aeration:
{row['aeration_vvm']} vvm

Biomass:
{row['biomass_g_l']} g/L

Temperature:
{row['temperature_c']} °C

pH:
{row['ph']}

Historical Intervention:
{row['intervention']}

Historical Outcome:
{row['outcome']}

This is synthetic historical demonstration data
created for the Bioprocess Incident Copilot.
"""


# ---------------------------------------------------------
# Load incidents
# ---------------------------------------------------------

def load_incidents():

    print("=" * 75)
    print("BIOPROCESS INCIDENT COPILOT")
    print("HISTORICAL INCIDENT INGESTION")
    print("=" * 75)

    print("\nLoading:")
    print(DATA_FILE)

    if not DATA_FILE.exists():

        print("\nERROR: incidents.csv was not found.")

        return

    df = pd.read_csv(DATA_FILE)

    print(f"\nFound {len(df)} historical incidents.")

    successful = 0
    failed = 0

    # -----------------------------------------------------
    # Send each incident to Hindsight
    # -----------------------------------------------------

    for index, row in df.iterrows():

        batch_id = row["batch_id"]

        print(
            f"\n[{index + 1}/{len(df)}] "
            f"Storing Batch {batch_id}..."
        )

        memory = create_incident_memory(row)

        try:

            remember_incident(
                incident_text=memory,
                context=(
                    f"Synthetic historical bioprocess "
                    f"incident - Batch {batch_id}"
                )
            )

            print(
                f"Batch {batch_id} stored successfully."
            )

            successful += 1

        except Exception as error:

            print(
                f"Batch {batch_id} failed."
            )

            print(error)

            failed += 1

    # -----------------------------------------------------
    # Summary
    # -----------------------------------------------------

    print("\n")
    print("=" * 75)
    print("INGESTION COMPLETE")
    print("=" * 75)

    print(f"Total incidents : {len(df)}")
    print(f"Successful      : {successful}")
    print(f"Failed          : {failed}")

    print("=" * 75)


if __name__ == "__main__":

    load_incidents()