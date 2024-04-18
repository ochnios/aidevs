import requests, json
from tools.aidevs import get_token, get_task, send_answer
from tools.openai import transcript

print('C02L05 functions')

# fetch token and task
token = get_token('functions')
task = get_task(token)
print('\ntask: ', task)

answer = {
    'name': 'addUser',
    'description': 'Function which adds user to the system',
    'parameters': {
        'type': 'object',
        'properties': {
            'name': {
                'type': 'string',
                'description': 'User name'
            },
            'surname': {
                'type': 'string',
                'description': 'User surname'
            },
            'year': {
                'type': 'integer',
                'description': 'Year of birth'
            }
        }
    }
}
print('\nanswer: ', answer)

# send answer
result = send_answer(token, answer)
print('\nresult: ', result)