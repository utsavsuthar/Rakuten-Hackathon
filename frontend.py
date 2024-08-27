import streamlit as st
from Scripts.recommendation_system_rakuten import recommend
from llm.prompting import prompt
from Scripts.update_dataset import extract_info
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
    df = pd.read_csv(csv_file_path)
    return "Function 3 executed: Welcome from Function 3!"

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
