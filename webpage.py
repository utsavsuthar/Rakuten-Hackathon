import streamlit as st

import google.generativeai as genai

# Define the API key (though it's better to handle this securely)
api_key = "AIzaSyA0-ftiGnQBYn1fP6eNafKIzVVCNKjZxrk"
genai.configure(api_key=api_key)

# Function to get response from the Gemini model
def get_gemini_response(logs):
    model = genai.GenerativeModel('gemini-pro')  # Pass API key if needed
    response = model.generate_content(logs)
    return response.text

# Streamlit app layout
st.title("CI/CD Pipeline Error Log Analyzer with Gemini")
st.write("Upload a CI/CD pipeline error log file to get possible answers.")

# File upload handler
uploaded_file = st.file_uploader("Choose a log file", type="txt", label_visibility="hidden")

if uploaded_file is not None:
    logs = uploaded_file.read().decode("utf-8")
    
    # Display the log file content
    st.subheader("Error Log Content:")
    st.text_area("Log Content", logs, height=200, label_visibility="hidden")

    # Process the logs with the Gemini model
    st.subheader("Model Output:")
    with st.spinner("Processing logs..."):
        output = get_gemini_response(logs)
        st.write(output)
