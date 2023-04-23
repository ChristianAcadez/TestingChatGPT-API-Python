import openai

openai.api_key = "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"

while True:

    prompt = input("\nIntroduce tu pregunta: ")

    if prompt == "exit":
        break

    completion = openai.Completion.create(model="text-davinci-003",
                                          prompt=prompt,
                                          temperature=0,
                                          max_tokens=3000)

    print(completion.choices[0].text)
