import openai

def to_string(a):
  return "{}".format(a)

def get_summary(raw_text):#string concatation ?
    # Set up the OpenAI API key
    openai.api_key = "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"

    # Define the text you want to summarize
    text = "good, nice, great, perfect, excellent, bad, worse, sketchy, shady, scam" 

    raw_text = map(to_string, raw_text)

    print(raw_text)

    print("the average tone of: {}".format(', '.join(raw_text)))

    # Use the OpenAI API to generate a summary of the text
    response = openai.Completion.create(
        engine="text-davinci-001",
        prompt="the average tone of: {}".format(', '.join(raw_text)),
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the summary from the API response
    tone = response["choices"][0]["text"].strip()

    # Print the summary
    print("Tone: " + tone)

    return tone