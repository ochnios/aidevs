import json
import requests
from tools.aidevs import get_token, get_task, send_answer
from tools.openai import chat, get_completion

print('C04L01 knowledge')

# define some useful functions
def get_population(country: str) -> int:
    api_response = requests.get(f'https://restcountries.com/v3.1/name/{country}')
    response_json = json.loads(api_response.text)
    return response_json[0]['population']

def get_exchange_rate(code: str) -> float:
    api_response = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/A/{code}?format=json')
    response_json = json.loads(api_response.text)
    return response_json['rates'][0]['mid']

# fetch token and task
token = get_token('knowledge')
task = get_task(token)
task_json = json.loads(task)
print('\ntask_json: ', task_json)
question = task_json['question']

# determine action to take using LLM
dispatcher_prompt = """Construct a JSON response according to the provided guidelines:
- The JSON must contain two properties: 'type' and 'details'.
- The value of 'type' can be one of the following: 'general', 'population', 'currency'
- 'details' should be filled according to 'type': For 'general' type, it should be the question asked by the user; 
for 'population', it should be the name of a country in English; for 'currency', it should be the currency code.

Examples:
Q: What is the population of France?
A: {"type": "population", "details": "France"}
---
Q: What is the current exchange rate for the dollar?
A: {"type": "currency", "details": "USD"}
---
Q: When did WW2 start?
A: {"type": "general", "details": "When did WW2 start?"}
---
"""
llm_response = chat(system=dispatcher_prompt, user=question, json_mode=True)
completion = get_completion(llm_response)
print('\naction dispatcher: ', completion)
action = json.loads(completion)

# prepare answer using external apis or llm knowledge
system_prompt = "Answer user question as truthfully as possible"
match str(action['type']).lower():
    case 'general':
        answer = get_completion(chat(system=system_prompt, user=action['details']))
    case 'population':
        answer = str(get_population(action['details']))
    case 'currency':
        answer = str(get_exchange_rate(action['details']))
    case _:
        print('Failed to determine action')
        exit()
print('\nanswer: ', answer)

# return answer
result = send_answer(token, answer)
print('\nresult: ', result)
