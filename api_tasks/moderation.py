import json
from tools.aidevs import get_token, get_task, send_answer
from tools.openai import moderate

# fetch token and  task
token = get_token('moderation')
task = get_task(token)
print(task)
input = json.loads(task)['input']
print(input)

# moderate given sentences
moderation = moderate(input)
results = json.loads(moderation)['results']
flagged = []
for r in results:
    flagged.append(1 if r['flagged'] else 0)
print(flagged)

# return answer
answer = send_answer(token, flagged)
print(answer)
