from services.email_service.messages_producer import MessagesProducer
from config.config import Config


def send_email_to_customer(subject, body):
    MessagesProducer.send_message(
        {"subject": subject, "body": body}, Config.app.kafka_topic_customer
    )


def send_email_to_owner(subject, body):
    MessagesProducer.send_message(
        {"subject": subject, "body": body}, Config.app.kafka_topic_owner
    )
