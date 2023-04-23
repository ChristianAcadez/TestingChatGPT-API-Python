import openai

openai.api_key = "" /*add your token here*/

while True:

    prompt = input("\nIntroduce tu pregunta: ")

    if prompt == "exit":
        break

    completion = openai.Completion.create(model="text-davinci-003",
                                          prompt=prompt,
                                          temperature=0,
                                          max_tokens=3000)

    print(completion.choices[0].text)
