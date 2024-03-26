import requests, json
import sys, os


base_url = 'https://tasks.aidevs.pl'


def get_token(taskname: str) -> str:
    apikey = os.getenv('AIDEVS_API_KEY')
    url = f"{base_url}/token/{taskname}"
    payload = {'apikey': apikey}
    response = requests.post(url, json=payload)
    token = json.loads(response.text)['token']
    # print(f'\nget_token: {token}')
    return token


def get_task(token: str) -> str:
    url = f"{base_url}/task/{token}"
    response = requests.get(url)
    # print(f'\nget_task: {response.text}')
    return response.text


def send_answer(token: str, answer) -> str:
    url = f"{base_url}/answer/{token}"
    payload = {'answer': answer}
    response = requests.post(url, json=payload)
    # print(f'\nsend_answer: {response.text}')
    return response.text


if __name__ == '__main__':
    action = sys.argv[1]
    if action == 'task':
        taskname = sys.argv[2]
        token = get_token(taskname)
        open('tasktoken', 'w').write(token)
        print(get_task(token))
    elif action == "answer":
        answer = sys.argv[2]
        token = open('tasktoken', 'r').read()
        print(send_answer(token, answer))
    else:
        print('Incorrect action')

