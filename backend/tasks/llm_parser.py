# import os
# import json
# from openai import OpenAI


# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# def parse_content(text,last_command="",task_list=None):
    
#     if task_list is None:
#         task_list = []


#     prompt = f"""
#     You are an AI task assistant.

#     Extract the intent and task from this sentence.

#     Possible intents:
#     create
#     update
#     delete

#     Sentence:
#     {text}

#     Return JSON like:
#     {{
#       "action": "...",
#       "task": "..."
#     }}
#     """

#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}]
#     )

#     output = response.choices[0].message.content

#     return json.loads(output)
import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)


def parse_content(text, last_command="", task_list=None):

    if task_list is None:
        task_list = []

    prompt = f"""
You are an AI task assistant.

Your job is to extract:
1. action
2. task

Use previous memory and existing tasks to resolve references.

Previous command:
{last_command}

Existing tasks:
{task_list}

Current user input:
{text}

Possible actions:
- create
- update
- delete

Understand references like:
- it
- adhi
- aa task
- that one
- previous one

Return ONLY valid JSON in this format:
{{
    "action": "create/update/delete",
    "task": "resolved task"
}}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    output = response.choices[0].message.content.strip()

    print("LLM raw output:", output)

    try:
        return json.loads(output)

    except:
        return {
            "action": "create",
            "task": text
        }