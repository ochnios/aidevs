import requests
import os


baseUrl = 'https://api.openai.com'


def moderate(input: str | list) -> bool:
    url = baseUrl + '/v1/moderations'
    payload = {'input': input, 'model': 'text-moderation-latest'}
    headers = {'Authorization': 'Bearer ' + os.getenv('OPENAI_API_KEY')}
    response = requests.post(url, headers=headers, json=payload)
    print('\nmoderate: {response.text}')
    return response.text