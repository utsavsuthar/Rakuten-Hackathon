
api_key = "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"
import openai
# Initialize the OpenAI API client
openai.api_key = api_key

def get_gpt4_turbo_response(prompt, examples, model="gpt-4o-mini"):
    try:
        # Construct messages for the conversation
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},  # System message for setting behavior
        ]

        # Add few-shot examples
        for example in examples:
            messages.append({"role": "user", "content": example["question"]})
            messages.append({"role": "assistant", "content": example["answer"]})

        # Add the new user prompt
        messages.append({"role": "user", "content": prompt})

        # Call the OpenAI API with the updated method
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            max_tokens=150,  # Adjust this as needed
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Few-shot examples
examples = [
    {"question": "What is the capital of France?", "answer": "The capital of France is Paris."},
    {"question": "Who wrote 'Hamlet'?", "answer": "William Shakespeare wrote 'Hamlet'."},
    {"question": "What is the boiling point of water?", "answer": "The boiling point of water is 100 degrees Celsius at sea level."},
]

# Example usage
if __name__ == "__main__":
    prompt = "What is the largest planet in our solar system?"
    response = get_gpt4_turbo_response(prompt, examples)
    print("GPT-4 Turbo Response:", response)
