import streamlit as st
from transformers import LlamaForCausalLM, LlamaTokenizer
# import torch

# Load the model and tokenizer (use LLaMA model equivalent)
# Example: Using a placeholder model as LLaMA 3 is not directly available
model_name = "meta-llama/Meta-Llama-3-8B"  # Replace with actual model path or name
tokenizer = LlamaTokenizer.from_pretrained(model_name)
model = LlamaForCausalLM.from_pretrained(model_name)

# Function to process logs with the model
def process_logs(logs):
    inputs = tokenizer(logs, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=100)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Streamlit app layout
st.title("CI/CD Pipeline Error Log Analyzer")
st.write("Upload a CI/CD pipeline error log file to get possible answers.")

# File upload handler
uploaded_file = st.file_uploader("Choose a log file", type="txt")

if uploaded_file is not None:
    # Read file
    logs = uploaded_file.read().decode("utf-8")
    
    # Display the log file content
    st.subheader("Error Log Content:")
    st.text_area("", logs, height=200)

    # Process the logs with the model
    st.subheader("Model Output:")
    with st.spinner("Processing logs..."):
        output = process_logs(logs)
        st.write(output)

