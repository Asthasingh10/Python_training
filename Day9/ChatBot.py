from openai import OpenAI
client = OpenAI()
# client.api_key=""
def chatbox(prompt):
    response=client.responses.create(
        model="gpt-4o",
        messages=[{"role":"user","content":prompt}]
    )
    return response.choices[0].message.content.strip()
if __name__=="__main__":
    while True:
        user_input=input("You: ")
        if user_input.lower() in ["quit","exit","bye"]:
            break
        response=chatbox(user_input)
        print("ChatBot: ",response.output_text)