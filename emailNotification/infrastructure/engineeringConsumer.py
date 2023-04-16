import json

from kafka import KafkaConsumer

from emailNotification.application.command.NotifyEngineeringCommand import NotifyEngineeringCommand
from emailNotification.application.service.NotifyEngineeringUseCase import NotifyEngineeringUseCase


class EngineeringConsumer:

    def __init__(self, notify_engineering_use_case: NotifyEngineeringUseCase):
        self.notify_engineering_use_case = notify_engineering_use_case

    def consume(self):
        consumer = KafkaConsumer('engineering',
                                 bootstrap_servers=['localhost:9092'],
                                 api_version=(0, 10)
                                 # ,consumer_timeout_ms=1000
                                 )

        for message in consumer:
            print(message.value)
            body = json.loads(message.value)
            command = NotifyEngineeringCommand(body['topic'], body['description'])
            self.notify_engineering_use_case.execute(command)
