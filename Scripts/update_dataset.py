import csv
import pandas as pd


# print("Last row:", last_row)



import re

# Provided pipeline error log text

# Incident Number,Company Name,Problem Title,Incident Severity,Error log,Pipeline Stage Summary,Primary Error,Solution
def extract_info(text):
    info = {}
    filepath = "Incidents/Incidents.csv"
    df = pd.read_csv(filepath)
    last_row = df.iloc[-1]

    # Define patterns to extract specific pieces of information
    patterns = {
        "Problem Title": r"Error Title:\s*(.*)",
        "Incident Severity": r"Severity:\s*(.*)",
        "Pipeline Stage Summary": r"Detailed Description:\s*(.*)",
        "Primary Error": r"Primary Error:\s*(.*)",
        "Solution": r"Possible Solutions:\s*([\s\S]*)"
    }

    # Extract information using the defined patterns
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            info[key] = match.group(1).strip()
    new_data = {
        "Incident Number": last_row['Incident Number'],
        "Company Name": last_row['Company Name'],
        "Error log": last_row['Error log'],
        "Problem Title": info.get("Problem Title", ""),
        "Incident Severity": info.get("Incident Severity", ""),
        "Pipeline Stage Summary": info.get("Pipeline Stage Summary", ""),
        "Primary Error": info.get("Primary Error", ""),
        "Solution": info.get("Solution", "")
    }
    df = df.astype('object')

    # Ensure the new columns are added if they are missing
    # for column in new_data.keys():
    #     if column not in df.columns:
    #         df[column] = pd.NA  # Add new columns with NA values if necessary

    # Update the last row
    # Note: Ensure `new_data` contains only keys that are present in DataFrame columns
    last_row_index = df.index[-1]

    # Create a Series with the new data, aligning the index with DataFrame columns
    update_series = pd.Series(new_data, index=df.columns)

    # Assign the Series to the last row
    df.loc[last_row_index] = update_series

    # Save the updated DataFrame back to the CSV file
    df.to_csv(filepath, index=False)

    print("Updated the last row with new information.")
