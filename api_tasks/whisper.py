import requests, json
from tools.aidevs import get_token, get_task, send_answer
from tools.openai import transcript

print('C02L04 whisper')

# fetch token and task
token = get_token('whisper')
task = get_task(token)
print('\ntask: ', task)

# fetch audio for transcription
task_data = requests.get('https://tasks.aidevs.pl/data/mateusz.mp3')
mp3 = task_data.content
with open('assets/C02L04_mateusz.mp3', 'wb') as file:
    file.write(mp3)
mp3 = open('assets/C02L04_mateusz.mp3', 'rb')

# generate transcrption
response = transcript(mp3)
print('\ntranscript response: ', response)
text = json.loads(response)['text']
print('\nanswer: ', text)

# send answer
result = send_answer(token, text)
print('\nresult: ', result)
