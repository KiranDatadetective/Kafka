from kafka import KafkaConsumer
from json import loads
import json

consumer = KafkaConsumer('testtopic', bootstrap_servers = ['localhost:9092'])


for message in consumer:
    print(message.value)