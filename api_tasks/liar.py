import json
from tools.aidevs import get_token, get_task, send_answer
from tools.openai import chat

print('C01L05 liar')

# fetch token and task
token = get_token('liar')
question = 'When World War 2 started?'
task = get_task(token, {'question': question})
print('\ntask: ', task)
task_answer = json.loads(task)['answer']
print(task_answer)

# check if answer is valid
response = chat(system='Is given answer true? Say only YES or NO.', 
                user=f'Q: {question}\nA: {task_answer}')
print(response)
answer = json.loads(response)['choices'][0]['message']['content']
print('\nanswer: ', answer)

# return answer
result = send_answer(token, answer)
print('\nresult: ', result)
