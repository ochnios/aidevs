import json
import requests
import os
from tools.aidevs import get_token, get_task, send_answer

print('C05L01 meme')

# fetch token and task
token = get_token('meme')
task = get_task(token)
task_json = json.loads(task)
print('\ntask_json: ', task_json)

# render image with RenderForm
headers = {'Content-Type': 'application/json', 'X-API-KEY': os.getenv('RENDERFORM_API_KEY')}
body = {'template': 'jolly-crabs-burrow-hastily-1187', 'data': {
    'text.text': task_json['text'],
    'image.src': task_json['image']
}}
response = requests.post(url='https://get.renderform.io/api/v2/render', json=body, headers=headers)
print('\nRenderForm response: ', response.text)
response_json = json.loads(response.text)

# send answer
result = send_answer(token, response_json['href'])
print('\nresult: ', result)
