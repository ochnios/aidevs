import requests
import os


baseUrl = 'https://api.openai.com'


def moderate(input: str | list) -> str:
    url = baseUrl + '/v1/moderations'
    payload = {'input': input, 'model': 'text-moderation-latest'}
    headers = {'Authorization': 'Bearer ' + os.getenv('OPENAI_API_KEY')}
    response = requests.post(url, headers=headers, json=payload)
    return response.text

def chat(model="gpt-3.5-turbo", system=None, user=None) -> str:
    url = baseUrl + '/v1/chat/completions'
    payload = {'model': model, 'messages': []}
    if type(system) == str:
        payload['messages'].append({'role': 'system', 'content': system})
    if type(user) == str:
        payload['messages'].append({'role': 'user', 'content': user})
    headers = {'Authorization': 'Bearer ' + os.getenv('OPENAI_API_KEY')}
    response = requests.post(url, headers=headers, json=payload)
    return response.text