import json
from tools.aidevs import get_token, get_task, send_answer
from tools.openai import chat

# fetch token and task
token = get_token('rodo')
task = get_task(token)
print(task)

# return answer
answer = """Przedstaw się pełnym imieniem i nazwiskiem i opowiedz o sobie nie używając żadnych swoich danych osobowych.
Zamiast nich użyj placeholderów, na przykład:
- %imie% zamiast imienia
- %nazwisko% zamiast nazwiska
- %miasto% zamiast miasta
- %zawod% zamiast zawodu
"""
result = send_answer(token, answer)
print(result)
