import streamlit as st
from Scripts.recommendation_system_rakuten import recommend
from llm.prompting import prompt
from Scripts.update_dataset import extract_info
import pandas as pd
import pdfkit
from io import BytesIO
# import getBuildLogs

# def generate_html(df):
#     row = df.iloc[0]
#     html_content = "<html><body>"
    
#     for column in df.columns:
#         html_content += f"<h2>{column}</h2>"
#         html_content += f"<p>{row[column]}</p>"
    
#     html_content += "</body></html>"
    
#     return html_content
# def generate_html(df):
#     # df = df[-1]
#     html_content = "<html><body>"
    
#     for index, row in df.iterrows():
#         html_content += f"<h1>Row {index + 1}</h1>"  # Adding row header
#         for column in df.columns:
#             html_content += f"<h2>{column}</h2>"
#             html_content += f"<p>{row[column]}</p>"
#         break
    
#     html_content += "</body></html>"
    
#     return html_content
wkhtmltopdf_path = '/usr/local/bin/wkhtmltopdf'
config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

def generate_html(df):
    # Get the last row of the DataFrame
    last_row = df.iloc[-1]
    html_content = "<html><body>"
    
    # Adding row header
    html_content += f"<h1>--------------------Root Cause Analysis Report--------------------</h1>"  # Adjust index if needed
    
    for column in df.columns:
        html_content += f"<h2>{column}</h2>"
        html_content += f"<p>{last_row[column]}</p>"
    
    html_content += "</body></html>"
    
    return html_content
# Function to convert HTML to PDF
def convert_html_to_pdf(html_content):
    pdf_file = pdfkit.from_string(html_content, False, configuration=config)
    return pdf_file

def display_dataframe(df):
    row = df.iloc[-1]
    
    for column in df.columns:
        # Display the column name as the heading
        # st.header(column)
        
        # # Display the value as a sentence
        # st.markdown(row[column])
        st.markdown(f"<h2 style='font-size: 30px;'>{column}</h2>", unsafe_allow_html=True)
        
        # Display the value as a sentence with larger font size
        # print(row[column])
        st.write(row[column])
        # st.markdown(f"<p style='font-size: 18px;'>{row[column]}</p>", unsafe_allow_html=True)
    # st.markdown(html, unsafe_allow_html=True)
    # Generate HTML content for the page
    # print(df['Error log'])
    html_content = generate_html(df)
    
    # Convert HTML to PDF
    pdf_file = convert_html_to_pdf(html_content)
    
    # Add a download button
    st.download_button(
        label="Download this page as PDF",
        data=pdf_file,
        file_name="RCA Report.pdf",
        mime="application/octet-stream"
    )


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
    def clean_text(text):
        if isinstance(text, str):
            # Remove markdown bold markers while preserving \n
            return text.replace("**", "")
        return text

    # Apply the clean_text function to all cells in the DataFrame
    formatted_data_df = df.applymap(clean_text)

    # Display the DataFrame with preserved newlines
    display_dataframe(formatted_data_df)
    st.write("Are you satisfied with the output?")
    st.button("Satisfactory")
       
    st.button("Just Fine")

    st.button("UnSatisfactory")
        
    return ""

# Center the image using markdown
# st.markdown("<img src="logo.jpeg"  class="center">", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')

with col2:
    st.image("logo_new.png", width=250)

with col3:
    st.write(' ')


st.title("RCA CoPilot: Let's solve the CI/CD issues)")

# Create a vertical layout for the buttons
st.header("Choose an option:")

# Create three columns for the buttons
col1, col2, col3 = st.columns(3)

# Place each button in a separate column
with col1:
    button1 = st.button("Recommendation System for CI/CD Pipeline Failures")

with col2:
    button2 = st.button("Automated Error Log Analysis & Resolution")

with col3:
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
