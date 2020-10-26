from kafka import KafkaConsumer
import json
from config.config import Config
from config.logger import get_app_logger
import sys, time


class MessagesConsumer(object):

    consumer = None

    @staticmethod
    def get_kafka_consumer():
        if MessagesConsumer.consumer is None:
            MessagesConsumer.consumer = KafkaConsumer(
                                           Config.configs.kafka_topic_owner,
                                           Config.configs.kafka_topic_customer,
                                           bootstrap_servers=[Config.configs.kafka_bootstrap_server],
                                           auto_offset_reset='earliest',
                                           consumer_timeout_ms=1000)
        return MessagesConsumer.consumer

    @staticmethod
    def consume_messages():
        logger = get_app_logger()

        messages = []
        attempts = 0
        while True:
            try:
                kafka_consumer = MessagesConsumer.get_kafka_consumer()
            except Exception as e:
                logger.critical(f'Error when trying to connect to Kafka Server: {e}')
                if attempts == Config.configs.max_attempts_kafka_server:
                    logger.critical("Max attempts to connect to Kafka Server reached. Email service stopping...")
                    sys.exit()
                else:
                    logger.critical(f'The service will retry in {str(Config.configs.global_sleep_time)} seconds')
                    time.sleep(Config.configs.global_sleep_time)
                    attempts += 1
            else:
                break

        for msg in kafka_consumer:
            try:
                record = json.loads(msg.value)
            except Exception as e:
                logger.critical(f'Json format error. Message discarded')
            else:
                messages.append(record)
        return messages

