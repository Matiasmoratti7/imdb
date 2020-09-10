import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config.config import Config
from config.logger import get_app_logger
from messages_consumer import MessagesConsumer
from config.logger import configure_logging
import time
import sys
from validators import validator

STAGE = 'ini/stage.ini'


def set_email_server():
    logger = get_app_logger()
    try:
        server = smtplib.SMTP_SSL()
        server = smtplib.SMTP_SSL(host=Config.configs.email_host, port=465)
        server.login(Config.configs.sender_email, Config.configs.sender_pswd)
    except Exception:
        logger.critical("Error when trying to login {}".format(Config.configs.sender_email))
        raise
    return server


def send_email(server, subject, body, receiver):
    logger = get_app_logger()

    msg = MIMEMultipart()
    msg['From'] = Config.configs.sender_email
    msg['To'] = receiver
    msg['Subject'] = "Imdb - " + subject

    msg.attach(MIMEText(body, 'plain'))

    attempts = 0
    email_sent = False
    while not email_sent:
        try:
            server.send_message(msg)
            email_sent = True
        except Exception:
            logger.critical("Error when trying to send email")

            if attempts == Config.configs.max_attempts_email:
                logger.critical("Max attempts to send an email reached. Email service stopping...")
                sys.exit()
            else:
                logger.critical(f'The service will retry in {str(Config.configs.global_sleep_time)} seconds')
                time.sleep(Config.configs.global_sleep_time)
                attempts += 1

    del msg


def run(config_file):
    # Set configs
    Config.load_from_file(config_file)

    # Configure logger
    logger = configure_logging()

    # Login email server
    email_server = set_email_server()

    # Send emails
    logger.critical("Email service starting...")
    messages = []
    while True:
        logger.critical("Email service is getting messages from Kafka server")
        messages.extend(MessagesConsumer.consume_messages())
        logger.critical("Email service will process {} messages".format(len(messages)))
        while messages:
            msg = messages.pop()
            if validator.validate(msg, validator.MESSAGE):
                send_email(email_server, msg['subject'], msg['body'], msg['receiver'])
        logger.critical("Email service finished processing new messages")
        time.sleep(Config.configs.global_sleep_time)


if __name__ == "__main__":
    run(config_file=STAGE)


