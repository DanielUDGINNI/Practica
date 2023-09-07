import openai
openai.api_key = "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"

conversation = ""

i = 1 
while (i !=0 ):
    question = input("Humano: ")
    conversation += "\nHumano: " + question + "\nAI:"
    response = openai.Completion.create(
        engine="davinci",
        prompt=conversation,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n","Humano:", "AI:"]
    )

    anwer = response.choices[0].text.strip()
    conversation += anwer
    print("AI: " + anwer + "\n")
