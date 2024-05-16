import requests, json
import os
from urllib3 import encode_multipart_formdata


baseUrl = 'https://api.openai.com'
session = requests.Session()

def moderate(input: str | list) -> str:
    url = baseUrl + '/v1/moderations'
    payload = {'input': input, 'model': 'text-moderation-latest'}
    headers = {'Authorization': 'Bearer ' + os.getenv('OPENAI_API_KEY')}
    response = session.post(url, headers=headers, json=payload)
    return response.text

def chat(model='gpt-3.5-turbo', system=None, user=None, json_mode=False, parsed=False) -> str:
    url = baseUrl + '/v1/chat/completions'
    payload = {'model': model, 'messages': []}
    if system is not None:
        payload['messages'].append({'role': 'system', 'content': system})
    if user is not None:
        payload['messages'].append({'role': 'user', 'content': user})
    if json_mode:
        payload['response_format'] = {'type': 'json_object'}
    headers = {'Authorization': 'Bearer ' + os.getenv('OPENAI_API_KEY')}
    response = session.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        print('An error occured while sending chat request, code: ', response.status_code)
        print('Response body: ', response.text)
    return json.loads(response.text)if parsed else response.text

def get_completion(model_response: str) -> dict:
    return json.loads(model_response)['choices'][0]['message']['content']

def embedding(input: str, model='text-embedding-ada-002') -> str:
    url = baseUrl + '/v1/embeddings'
    payload = {'model': model, 'input': input, 'encoding_format': 'float'}
    headers = {'Authorization': 'Bearer ' + os.getenv('OPENAI_API_KEY')}
    response = session.post(url, headers=headers, json=payload)
    return response.text

def transcript(data, model='whisper-1') -> str:
    url = baseUrl + '/v1/audio/transcriptions'
    payload = {'model': model}
    files = {'file': data}
    headers = {'Authorization': 'Bearer ' + os.getenv('OPENAI_API_KEY')}
    response = session.post(url, data=payload, headers=headers, files=files, verify=False)
    return response.text
