import json
from tools.aidevs import get_token, get_task, send_answer
from tools.openai import chat, get_completion
from datetime import datetime

print('C04L03 gnome')

# fetch token and task
token = get_token('gnome')
task = get_task(token)
task_json = json.loads(task)
print('\ntask_json: ', task_json)
msg = task_json['msg']
url = task_json['url']

# determine hat color using vision
# https://platform.openai.com/docs/guides/vision
system_prompt = 'Return ONLY color name or ERROR string if there is not gnome in the image.'
user_message = [
    {'type': 'text', 'text': msg},
    {
        'type': 'image_url',
        'image_url': {
            'url': url
        }
    }
]
llm_response = chat(model='gpt-4-turbo', system= system_prompt, user=user_message)
completion = get_completion(llm_response)
print('\nfull completion response: ', llm_response)
print('\nanswer: ', completion)

# return answer
result = send_answer(token, completion)
print('\nresult: ', result)
