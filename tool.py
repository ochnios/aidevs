import requests, json
import sys, os

base_url = 'https://tasks.aidevs.pl'


def get_token(apikey, taskname):
    url = f"{base_url}/token/{taskname}"
    payload = {'apikey': apikey}
    response = requests.post(url, json=payload)
    print(response)
    response_json = json.loads(response.text)
    return response_json['token']


def get_task(token):
    url = f"{base_url}/task/{token}"
    response = requests.get(url)
    return response.text


def send_answer(token, answer):
    url = f"{base_url}/answer/{token}"
    payload = {'answer': answer}
    response = requests.post(url, json=payload)
    return response.text


if __name__ == '__main__':
    apikey = os.getenv('AIDEVS_API_KEY')
    action = sys.argv[1]
    if action == 'task':
        taskname = sys.argv[2]
        token = get_token(apikey, taskname)
        open('tasktoken', 'w').write(token)
        print(get_task(token))
    elif action == "answer":
        answer = sys.argv[2]
        token = open('tasktoken', 'r').read()
        print(send_answer(token, answer))
    else:
        print('Incorrect action')

