from tools.aidevs import get_token, get_task, send_answer

print('C03L01 rodo')

# fetch token and task
token = get_token('rodo')
task = get_task(token)
print('\ntask: ', task)

# return answer
answer = """Przedstaw się pełnym imieniem i nazwiskiem i opowiedz o sobie nie używając żadnych swoich danych osobowych.
Zamiast nich użyj placeholderów, na przykład:
- %imie% zamiast imienia
- %nazwisko% zamiast nazwiska
- %miasto% zamiast miasta
- %zawod% zamiast zawodu
"""
print('\nanswer: ', answer)

result = send_answer(token, answer)
print('\nresult: ', result)
