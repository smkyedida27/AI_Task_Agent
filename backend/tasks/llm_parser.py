import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def parse_content(text):

    prompt = f"""
    You are an AI task assistant.

    Extract the intent and task from this sentence.

    Possible intents:
    create
    update
    delete

    Sentence:
    {text}

    Return JSON like:
    {{
      "action": "...",
      "task": "..."
    }}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    output = response.choices[0].message.content

    return eval(output)