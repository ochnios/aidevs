import json
from tools.aidevs import get_token, get_task, send_answer
from tools.openai import embedding

print('C02L03 embedding')

# fetch token and task
token = get_token('embedding')
task = get_task(token)
print('\ntask: ', task)

# generate embedding for input
input = 'Hawaiian pizza'
response = embedding(input)
answer = json.loads(response)['data'][0]['embedding']
print('\nanswer: ', answer)

# return answer
result = send_answer(token, answer)
print('\nresult: ', result)
