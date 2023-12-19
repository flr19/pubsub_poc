import os
from google.cloud import pubsub_v1
credentials_path = 'farah-394715-085481857d17.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

publisher = pubsub_v1.PublisherClient()
topic_path = 'projects/farah-394715/topics/first-topic'

data = 'your message'
data = data.encode('utf-8')
attributes = {
    'DIVISION_ID': '2',
    'FILE_ID': 'OMS_EXE_I365_EXE_ORDERS.2023121807574849774.txt',
    'RELEASE_ID': '236323'
}


future = publisher.publish(topic_path, data, **attributes)
print(f'published message id {future.result()}')

