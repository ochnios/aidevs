import json
import requests
from tools.aidevs import get_token, get_task, send_answer
from tools.openai import chat, get_completion

print('C03L05 people')

# fetch token and task
token = get_token('people')
task = get_task(token)
print('\ntask: ', task)

task_json = json.loads(task)
data_url = task_json['data']
question = task_json['question']
print('question: ', question)

# find out person name
# TODO with function calling
system_prompt = """Zwróć JSON zawierający pola name i surname na podstawie pytania użytkownika.
Zamieniaj zdrobnienia i odmiany imienia na jego podstawową formę. Przykłady:
---
Q: Gdzie mieszka Szymek Szklanka?
A: {"name": "Szymon", "surname": "Szklanka"}
---
Q: Jaki kolor podoba się Kasi Abackiej?
A: {"name": "Katarzyna", "surname": "Abacka"}
"""
for i in range(5):
    try:
        response = chat(system=system_prompt, user=question)
        completion = get_completion(response)
        print('completion: ', completion)
        completion_json = json.loads(completion)
        name = completion_json['name']
        surname = completion_json['surname']
        break
    except Exception as e:
        print('An error occured: ', e)

# download database

people = requests.get(url=data_url)
people_json = json.loads(people.content)
print("people len: ", len(people_json))

# filter entries mentioning person
filter_object = filter(lambda x: name in x['imie'] and surname in x['nazwisko'], people_json)
filtered_people = list(filter_object)
print('filtered people: ', filtered_people)

# answer question with filtered person info
system_prompt = f"""Odpowiedz na pytanie użytkownika na podstawie podanego kontekstu.
```context
{filtered_people[0]}
```
"""
response = chat(system=system_prompt, user=question)
answer = get_completion(response)
print('\nanswer: ', answer)

# return answer
result = send_answer(token, answer)
print('\nresult: ', result)
