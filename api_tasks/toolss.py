import json
from tools.aidevs import get_token, get_task, send_answer
from tools.openai import chat, get_completion
from datetime import datetime

print('C04L02 tools')

# fetch token and task
token = get_token('tools')
task = get_task(token)
task_json = json.loads(task)
print('\ntask_json: ', task_json)
question = task_json['question']

# determine action to take using LLM
formatted_date = datetime.today().strftime("%A, %d %B %Y (%Y-%m-%d)")
dispatcher_prompt = f"""Construct a JSON response according to the provided guidelines:
- The JSON must contain two properties: 'tool' and 'desc' and 'date' when selected tool is ToDo.
- The value of 'tool' can be one of the following: 'ToDo', 'Calendar'
- 'desc' should be filled according to 'tool': For 'ToDo' tool, it should be task extracted from user question; 
for 'Calendar', it should be the event name extracted from user question.
- For 'Calendar' tool return also 'date' in YYYY-MM-DD format
- For 'ToDo' tool do not return 'date' field

- Answer in users language

Today is {formatted_date}.

Examples:
Q: Przypomnij mi, że mam kupić mleko
A: {{"tool":"ToDo","desc":"Kup mleko"}}
---
Q: Jutro mam spotkanie z Marianem?
A: {{"tool":"Calendar","desc":"Spotkanie z Marianem","date":"2024-05-07"}}
---
"""

llm_response = chat(model='gpt-4-turbo', system=dispatcher_prompt, user=question, json_mode=True)
completion = get_completion(llm_response)
print('\nanswer: ', completion)

# return answer
result = send_answer(token, json.loads(completion))
print('\nresult: ', result)
