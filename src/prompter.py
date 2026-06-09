from dotenv import load_dotenv
from google import genai
from google.genai import types
import yaml
import os
from log import log
from generate_hints import every_ith_word

load_dotenv()

def prompt_ith_word(i, hints) -> str:
    prompt = ''
    with open('prompt_pieces.yml','r') as file:
        config = yaml.safe_load(file)
        prompt = config['ith_word_prompt']

    prompt = prompt.replace('***ith***', str(i))
    prompt += str(hints)

    client = get_client()
    response = generate_content(client, prompt)

    log_message = {}
    log_message['hints'] = ' '.join(hints)
    log_message['i'] = i
    log_message['prompt'] = prompt
    log_message['response'] = response['text']
    log_message['temperature'] = response['temperature']
    log_message['model'] = response['model']

    file_path = f'src/logs/ith_word/{i}.log'

    log(file_path, log_message)
    return response

def get_client() -> genai.Client:
    llm_api_key = os.getenv("LLM_API_KEY")

    retry_options = types.HttpRetryOptions(
        attempts = 10,
        initial_delay = 1.0,
        max_delay=60,
        http_status_codes=[500,502,503,504,429]
    )

    client = genai.Client(
        api_key = llm_api_key,
        http_options = types.HttpOptions(retry_options=retry_options),
    )

    return client

def generate_content(client, prompt) -> str:
    llm_model = os.getenv("LLM_MODEL")
    temperature = 0.0

    result = client.models.generate_content(
        model = llm_model,
        contents = prompt,
        config=types.GenerateContentConfig(
            temperature=temperature
        )
    )

    return {"text": result.text, "temperature":temperature, "model":llm_model}


if __name__ == '__main__':
    i = 3
    hints = every_ith_word('passages/passage_1.txt',i)
    prompt_ith_word(i,hints)

    