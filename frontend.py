import streamlit as st
from Scripts.recommendation_system_rakuten import recommend
from llm.prompting import prompt
from Scripts.update_dataset import extract_info
import pandas as pd
# import getBuildLogs

# Define the three functions to be called when each button is clicked
def function1():
    with open('ParsedLogs/summ_log.txt', 'r') as file:
        contents = file.read()
    recommendations = recommend(contents)
    return recommendations

def function2():
    with open('ParsedLogs/summ_log.txt','r') as file:
        ex_2=file.read()
    result = prompt(ex_2)
    # print(result)
    # print(dir(result))
    extract_info(result.text)
    return result.text

def function3():
    csv_file = 'Incidents/Incidents.csv'
    df = pd.read_csv(csv_file)

    # Get the last row of the DataFrame
    last_row = df.iloc[-1]

    # Create a Streamlit form with editable text fields
    st.title("Editable Text Fields with Last Row Data")

    # Initialize a form in Streamlit
    with st.form(key='my_form'):
        # Create editable text fields for each column in the last row
        form_data = {}
        for column in df.columns:
            # Display the text field prefilled with the last row's data
            form_data[column] = st.text_input(column, value=str(last_row[column]))

        # Add a submit button
        submit_button = st.form_submit_button(label='Submit')

    # Handle the form submission
    if submit_button:
        st.write("Form submitted with the following data:")
        st.write(form_data)

        # Optionally, update the last row in the DataFrame and save it back to the CSV file
        for column, value in form_data.items():
            df.at[df.index[-1], column] = value

        df.to_csv(csv_file_path, index=False)
        st.success("Data updated in the CSV file.")

# Create the Streamlit app layout
st.title("RCA CoPilot: Let's solve the CI/CD issues together :)")

#call the function to get the log files fron jenkins
# getBuildLogs.printfn()
# print("call completed")

# Create a horizontal layout for the buttons
col1, col2, col3 = st.columns(3)

# Initialize a variable to hold the output
output = ""

# Add buttons to the layout
with col1:
    if st.button("Button 1"):
        output = function1()

with col2:
    if st.button("Button 2"):
        output = function2()

with col3:
    if st.button("Button 3"):
        output = function3()

# Display the output below the buttons
st.write(output)
