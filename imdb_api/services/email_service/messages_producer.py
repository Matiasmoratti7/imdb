from kafka import KafkaProducer
from exceptions.errors import CustomError
import json
from config.config import Config


class MessagesProducer(object):

    producer = None

    @staticmethod
    def get_kafka_producer():
        if not MessagesProducer.producer:
            try:
                MessagesProducer.producer = KafkaProducer(
                    bootstrap_servers=[Config.app.kafka_bootstrap_server],
                    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
                )
            except Exception:
                raise CustomError("Error when trying to connect to Kafka Server", 500)
        return MessagesProducer.producer

    @staticmethod
    def send_message(json_message, topic):
        producer = MessagesProducer.get_kafka_producer()
        try:
            producer.send(topic, json_message)
            producer.flush()
        except Exception:
            raise CustomError(
                "Error when trying to connect to send message to Kafka Server", 500
            )
