import json
from tools.aidevs import get_token, get_task, send_answer

print('C04L05 ownapipro')

# fetch token and task
token = get_token('ownapipro')
task = get_task(token)
task_json = json.loads(task)
print('\ntask_json: ', task_json)

exit()
# send my api address as answer
result = send_answer(token, "https://hook.eu2.make.com/{mywebhook}")
print('\nresult: ', result)
