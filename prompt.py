import openai

# Set OpenAI API key
openai.api_key = "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"

# Define function to send prompt and receive response
def get_response(prompt):
    # Set the parameters for the API call
    model = "text-davinci-002"
    temperature = 0.5
    max_tokens = 50
    stop = "\n"

    # Generate a response
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        stop=stop
    )

    # Get the generated text from the response
    answer = response.choices[0].text.strip()

    # Return the answer
    return answer

# Define function to send prompt and receive response
def send_prompt_and_receive_answer():
    # Get the prompt from the user
    prompt = input("Enter your prompt: ")

    # Get the response from the OpenAI API
    answer = get_response(prompt)

    # Send the answer to the user
    print("Answer:", answer)

# Call the function to send prompt and receive answer
send_prompt_and_receive_answer()