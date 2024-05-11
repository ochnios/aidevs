import json
from tools.aidevs import get_token, get_task, send_answer
from tools.openai import chat, get_completion
from datetime import datetime

print('C04L04 ownapi')

# fetch token and task
token = get_token('ownapi')
task = get_task(token)
task_json = json.loads(task)
print('\ntask_json: ', task_json)

# send my api address as answer
result = send_answer(token, "https://hook.eu2.make.com/{mywebhook}")
print('\nresult: ', result)
