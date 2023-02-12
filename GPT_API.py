import openai


# Set up the OpenAI API key
openai.api_key = "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"

# Define the text you want to summarize
text = "good, nice, great, perfect, excellent, bad, worse, sketchy, shady, scam" 

# Use the OpenAI API to generate a summary of the text
response = openai.Completion.create(
engine="text-davinci-001",
prompt="the average tone of: " + text,
max_tokens=100,
n=1,
stop=None,
temperature=0.5,
)

# Extract the summary from the API response
tone = response["choices"][0]["text"].strip()

# Print the summary
print("Tone: " + tone)