import os
from google.cloud import pubsub_v1
from concurrent.futures import TimeoutError

credentials_path = 'farah-394715-085481857d17.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

timeout = 5.0

subscriber = pubsub_v1.SubscriberClient()
subscription_path = 'projects/farah-394715/subscriptions/first-topic-sub'

def callback(message):
    print(f'Received message: {message}')
    print(f'data: {message.data.decode("utf-8")}') 

    if message.attributes:
        print("Attributes:")
        for key in message.attributes:
            value = message.attributes.get(key)
            print(f"{key}: {value}")
            if (key == "DIVISION_ID"):
                print("true")

    #message.ack()           


streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f'Listening for messages on {subscription_path}')


with subscriber:                                                # wrap subscriber in a 'with' block to automatically call close() when done
    try:
        # streaming_pull_future.result(timeout=timeout)
        streaming_pull_future.result()                          # going without a timeout will wait & block indefinitely
    except TimeoutError:
        streaming_pull_future.cancel()                          # trigger the shutdown
        streaming_pull_future.result()                          # block until the shutdown is complete
    except Exception as e:
        print(f"Error: {e}")


