import os
from dotenv import load_dotenv
from groq import Groq

# load .env variables
load_dotenv()

# read api key
# like this
api_key = os.getenv("GROQ_API_KEY")

# create client
client = Groq(api_key=api_key)

print("AI Chat started (type 'exit' to stop)\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chat ended")
        break

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    answer = response.choices[0].message.content

    print("AI:", answer)