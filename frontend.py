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
    data_df = recommend(contents)

    st.title("Top 3 Similar Incidents & Solutions!")
    formatted_data_df = data_df.applymap(
        lambda x: x.replace("**", "").replace("**", "") if isinstance(x, str) else x
    )
    formatted_data_df = formatted_data_df.applymap(
        lambda x: x.replace("\n", "<br>") if isinstance(x, str) else x
    )

    # Convert the formatted DataFrame to HTML
    html = formatted_data_df.to_html(index=False, escape=False, border=1)

    # Display the HTML in Streamlit
    st.markdown(html, unsafe_allow_html=True)

    return ''

def function2():
    with open('ParsedLogs/summ_log.txt','r') as file:
        ex_2=file.read()
    result = prompt(ex_2)
    
    # print(result_filterd)
    # print(dir(result))
    extract_info(result.text)
    return result.text

def function3():
    csv_file = 'Incidents/Incidents.csv'
    df = pd.read_csv(csv_file)

    # Get the last row of the DataFrame
    # new_df = df.tail(1).reset_index(drop=True)
    new_df = df.tail(1).reset_index(drop=True)
    row = new_df.iloc[0]
    for column in new_df.columns:
        # Display the column name as the heading
        st.header(column)
        
        # Display the value as a sentence
        st.markdown(row[column])

# Display the new DataFrame without showing the index (row number)
# print("\nNew DataFrame with only the last row (index not displayed):")
    # new_df.to_string(index=False)
    # st.table(new_df)
    return ""
            


st.title("RCA CoPilot: Let's solve the CI/CD issues together :)")

# Create a vertical layout for the buttons
st.header("Choose an option:")
button1 = st.button("Recommendation System for CI/CD Pipeline Failures")
button2 = st.button("Automated Error Log Analysis & Resolution")
button3 = st.button("Automated Root Cause Analysis Reports")

# Initialize a variable to hold the output
output = ""

# Check which button is clicked and call the corresponding function
if button1:
    output = function1()
elif button2:
    output = function2()
elif button3:
    output = function3()


# Display the output below the buttons
st.write(output)
