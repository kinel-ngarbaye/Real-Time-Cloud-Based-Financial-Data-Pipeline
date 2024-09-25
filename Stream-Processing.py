from google.cloud import pubsub_v1
import json

project_id = "your-gcp-project-id"
subscription_id = "financial-data-subscription"

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)

def callback(message):
    data = json.loads(message.data)
    print(f"Received: {data}")
    analyze_stock_data(data)
    message.ack()

# Simple analysis function
def analyze_stock_data(data):
    if data['price'] > 1000:
        print(f"Alert: {data['symbol']} crossed $1000 with price {data['price']}!")

# Start consuming messages
streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print("Listening for messages...")

with subscriber:
    try:
        streaming_pull_future.result()
    except KeyboardInterrupt:
        streaming_pull_future.cancel()
