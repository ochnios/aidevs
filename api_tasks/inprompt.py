import json
from tools.aidevs import get_token, get_task, send_answer
from tools.openai import chat, get_completion

print('C02L02 inprompt')

# fetch token and task
token = get_token('inprompt')
task = get_task(token)
print('\ntask: ', task)

task_json = json.loads(task)
input = task_json['input']
question = task_json['question']
print('question: ', question)

# find out person name
response = chat(system='Return ONLY name which is given in user question.', user=question)
name = get_completion(response)
print('name: ', name)

# filter sentences mentioning person
filter_object = filter(lambda x: name in x, input)
filtered_input = list(filter_object)
print('filtered_input: ', filtered_input)

# answer question with filtered person info
response = chat(system=f"Basing on given context, answer user question.\n```context\n{filtered_input[0]}\n```",
                user=question)
answer = get_completion(response)
print('\nanswer: ', answer)

# return answer
result = send_answer(token, answer)
print('\nresult: ', result)
