import requests, json
from tools.aidevs import get_token, get_task, send_answer
from tools.openai import transcript

# fetch token and task
token = get_token('whisper')
task = get_task(token)

# fetch audio for transcription
task_data = requests.get('https://tasks.aidevs.pl/data/mateusz.mp3')
mp3 = task_data.content
with open('assets/mateusz.mp3', 'wb') as file:
    file.write(mp3)
mp3 = open('assets/mateusz.mp3', 'rb')

# generate transcrption
response = transcript(mp3)
print(response)
text = json.loads(response)['text']

# send answer
result = send_answer(token, text)
print(result)
