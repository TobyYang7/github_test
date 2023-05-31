import openai
import os

# Set API key
openai.api_key = os.environ["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"]
# Generate text in French
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Bonjour, comment ça va?",
    max_tokens=50,
    model="t5-small",
    temperature=0.5,
    n=1,
    stop=None,
    frequency_penalty=0,
    presence_penalty=0
)

# Print the generated text
print(response.choices[0].text)
# FIX
