import json
import requests
from tools.aidevs import get_token, get_task, send_answer
from tools.openai import chat

print('C05L02 optimaldb')

# fetch token and task
token = get_token('optimaldb')
task = get_task(token)
task_json = json.loads(task)
print('\ntask_json: ', task_json)

# download knowledge database
knowledge = requests.get('https://tasks.aidevs.pl/data/3friends.json').text
print('\nsize of knowledge: ', len(knowledge))
knowledge_json = json.loads(knowledge)


# monitor usage
prompt_tokens = 0
completion_tokens = 0
def record_usage(response_json: dict) -> None:
    global prompt_tokens, completion_tokens
    prompt_tokens += response_json['usage']['prompt_tokens']
    completion_tokens += response_json['usage']['completion_tokens']

def print_usage():
    print('\nrecorded usage:')
    print('\tprompt_tokens:', prompt_tokens)
    print('\tcompletion_tokens', completion_tokens)

# compress database
recognizer_prompt = 'Your goal is to return ONLY name of person mentioned in the given text.'
compressor_prompt = '''Twoim zadaniem jest streszczenie podanego tekstu aby był jak najkrótszy. W odpowiedzi pomijaj imię użytkownika. Przykład: 
Q: "Kiedy zapytasz go o ulubioną grę, Zygfryd bez wahania odpowie, że jest nią 'Terra Mystica'."
A: "Ulubiona gra to Terra Mystica."
'''

def split_into_subarrays(arr, subarray_length):
    num_full_subarrays = len(arr) // subarray_length
    remainder = len(arr) % subarray_length
    subarrays = []
    for i in range(num_full_subarrays):
        start_index = i * subarray_length
        end_index = start_index + subarray_length
        subarrays.append(arr[start_index:end_index])
    if remainder:
        subarrays.append(arr[-remainder:])
    
    return subarrays

def compress_info(info_list: list[str]) -> str:
    response = chat(system=recognizer_prompt, user=info_list[0], parsed=True)
    name = response['choices'][0]['message']['content']
    record_usage(response)
    compressed = '### ' + name + '\n'
    print('\nstarting compression for: ', name)
    for info_sublist in split_into_subarrays(info_list, 10):
        info = ''.join(info_sublist).replace(name.strip(), '').replace('  ', ' ')
        response = chat(system=compressor_prompt, user=info, parsed=True)
        compressed_info = response['choices'][0]['message']['content']
        record_usage(response)
        print(info,' -> ', compressed_info)
        compressed += compressed_info
    return compressed

zygfryd_compressed = compress_info(knowledge_json['zygfryd'])
print_usage()

stefan_compressed = compress_info(knowledge_json['stefan'])
print_usage()

ania_compressed = compress_info(knowledge_json['ania'])
print_usage()


# merge compressed knowledge about people
knowledge_compressed = zygfryd_compressed + stefan_compressed + ania_compressed
print('size after compression:', len(knowledge_compressed))

# send answer
result = send_answer(token, knowledge_compressed)
print('\nresult: ', result)
