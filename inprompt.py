import json
from tools.aidevs import get_token, get_task, send_answer
from tools.openai import chat

# fetch token and task
token = get_token('inprompt')
task = get_task(token)
# print(task)

task_json = json.loads(task)
input = task_json['input']
question = task_json['question']
print(question)

# find out person name
response = chat(system='Return ONLY name which is given in user question.', user=question)
name = json.loads(response)['choices'][0]['message']['content']
print(name)

# filter sentences mentioning person
filter_object = filter(lambda x: name in x, input)
filtered_input = list(filter_object)
print(filtered_input)

# answer question with filtered person info
response = chat(system=f"Basing on given context, answer user question.\n```context\n{filtered_input[0]}\n```",
                user=question)
answer = json.loads(response)['choices'][0]['message']['content']

# return answer
result = send_answer(token, answer)
print(result)
