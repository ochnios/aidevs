import json
from tools.aidevs import get_token, get_task, send_answer
from tools.openai import chat

# fetch token and task
token = get_token('blogger')
task = get_task(token)
print(task)
blog = json.loads(task)['blog']
print(blog)

# prepare blog posts
answers = []
for chapter in blog:
    response = chat(system='Przygotuj bardzo krótki wpis na bloga na temat podany przez użytkownika.', user=chapter)
    print(response)
    answers.append(json.loads(response)['choices'][0]['message']['content'])

# return answer
result = send_answer(token, answers)
print(result)
