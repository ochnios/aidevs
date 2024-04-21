import requests
import json
from tools.aidevs import get_token, get_task, send_answer
from tools.openai import chat, get_completion, embedding
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance

print('C03L04 search')

client = QdrantClient(url='http://localhost:6333')
collection_name = 'archiwum_aidevs'

def load():
    # download link archive
    archive = requests.get('https://unknow.news/archiwum_aidevs.json')
    archive_json = json.loads(archive.content)
    # print('archive: ', archive_json)
    print('archive: ', len(archive_json))

    points = []
    for idx, item in enumerate(archive_json):
        print(f'embedding {item['title']}')
        text = item['title'] + item['info']
        response = embedding(text, model='text-embedding-3-small')
        embedded = json.loads(response)['data'][0]['embedding']
        print(embedded[:10])
        points.append(
            PointStruct(
                id=idx, 
                vector=embedded, 
                payload={"text": text, "url": item['url'], "data": item['date']})
        )

    client.create_collection(
        collection_name,
        vectors_config=VectorParams(
            size=1536,
            distance=Distance.COSINE,
        ),
    )
    client.upsert(collection_name, points)

# load()

# fetch token and task
token = get_token('search')
task = get_task(token)
print('\ntask: ', task)
question = json.loads(task)['question']

# generate question embedding
response = embedding(question, model='text-embedding-3-small')
question_embedding = json.loads(response)['data'][0]['embedding']
print('question: ', question)
print('question embedding: ', question_embedding[:10])

# search in qdrant
search_result = client.search(
    collection_name=collection_name, query_vector=question_embedding, limit=1
)
print('\nsearch result: ', search_result)
answer = search_result[0].payload['url']
print('answer: ', answer)

# send answer
result = send_answer(token, answer)
print('\nresult: ', result)