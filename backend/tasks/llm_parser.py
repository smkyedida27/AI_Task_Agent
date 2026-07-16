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
import certifi
import httpx


load_dotenv()






api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)
http_client = httpx.Client(verify=certifi.where())
client  = Groq(api_key = api_key,http_client=http_client)


def parse_content(text, last_command="", task_list=None):

    if task_list is None:
        task_list = []

    prompt = f"""
You are an AI semantic parser for a task assistant.

Your only job is to understand:
1. user intention
2. task reference

Possible intentions:
- new_task → user wants to add a task
- completed_task → user says task is done
- remove_task → user wants to delete a task
- fetch_tasks → user wants to see current or pending tasks

Previous command:
{last_command}

Existing tasks:
{task_list}

Current user input:
{text}

Understand any natural language including Telugu-English mixed language.

Return ONLY valid JSON:
{{
    "intent": "new_task/completed_task/remove_task/fetch_tasks",
    "task_reference": "task meaning or empty string"
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
            "intent": "new_task",
            "task_reference": text
        }