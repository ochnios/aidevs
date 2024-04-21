import json
import requests
from tools.aidevs import get_token, get_task, send_answer
from tools.openai import chat, get_completion

print('C03L03 whoami')


system = 'Twoim zadaniem jest odgadnięcie o kogo chodzi na podstawie wskazówek dostarczonych przez użytkownika. Jeśli nie wiesz o kogo chodzi odpowiadasz tylko i wyłącznie frazą NIE. Jeśli wiesz o kogo chodzi, to po prostu mówisz co to za osoba. Możesz odpowiedzieć tylko i wyłącznie gdy masz absolutną pewność o kogo chodzi, w przeciwnym wypadku odpowiadaj NIE. Nie próbuj zgadywać gdy użytkownik podaje zbyt mało faktów na temat danej osoby.'
hints = ''
for i in range(10):
    # fetch token and task
    token = get_token('whoami')
    task = get_task(token)
    print(f'\ntask[{i}]: ', task)
    task_json = json.loads(task)
    hints += '- ' + task_json['hint'] + '\n'
    print('hints: ', hints)
    # send context and question to the model
    llm_response = chat(system=system, user=hints, model="gpt-4")
    answer = get_completion(llm_response)
    print(f'\nanswer[{i}]: ', answer)
    if "NIE" in answer:
        continue
    else:
        # return answer
        result = send_answer(token, answer)
        print('\nresult: ', result)
        break
