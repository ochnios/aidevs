import json
import requests
from tools.aidevs import get_token, get_task, send_answer
from tools.openai import chat, get_completion

# fetch token and task
token = get_token('scraper')
task = get_task(token)
print(task)
task_json = json.loads(task)
input = task_json['input']
question = task_json['question']

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
# try to scrape article from given webpage
for i in range(10):
    print("Attempt ", i)
    try:
        response = requests.get(input, headers=headers)
        response.raise_for_status()
        break
    except requests.RequestException as e:
        print('An error occured: ', e)
print(response.content)

# send context and question to the model
llm_response = chat(system=f"Basing on given context, answer user question ultra briefly.\n```context\n{response.text}\n```",
                user=question)
answer = get_completion(llm_response)
print(answer)

# return answer
result = send_answer(token, answer)
print(result)
