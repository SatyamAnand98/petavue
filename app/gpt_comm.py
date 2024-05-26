from dotenv import load_dotenv
from openai import OpenAI

from store.logging import configure_logger

load_dotenv()

client = OpenAI()
logger = configure_logger()

def generate_result_from_prompt(prompt: str, role_prompt: str = None, gpt_model: str = "gpt-3.5-turbo"):
    try:
        msg = []
        if role_prompt:
            msg.append({
                "role": "system",
                "content": role_prompt
            })
        
        msg.append({
            "role": "user",
            "content": prompt
        })

        response = client.chat.completions.create(
            messages=msg,
            max_tokens=1000,
            model=gpt_model,
        )

        response_msg = response.choices[0].message.content

        return response_msg
    except Exception as e:
        logger.error(e)
