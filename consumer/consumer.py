import pika
import smtplib
import json
import time

from email.mime.text import MIMEText

RABBITMQ_HOST = "rabbitmq"
QUEUE_NAME = "emails"

SMTP_HOST = "mailhog"
SMTP_PORT = 1025


def connect_rabbitmq():
    while True:
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=RABBITMQ_HOST)
            )

            print("Conectado ao RabbitMQ!")

            return connection

        except Exception as e:
            print("Erro ao conectar RabbitMQ:", e)
            time.sleep(5)


def send_email(to, subject, body):

    msg = MIMEText(body, "html")

    msg["Subject"] = subject
    msg["From"] = "empresa@teste.com"
    msg["To"] = to

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.send_message(msg)

    print(f"Email enviado para {to}")


def callback(ch, method, properties, body):

    data = json.loads(body)

    send_email(
        data["to"],
        data["subject"],
        data["body"]
    )

    ch.basic_ack(delivery_tag=method.delivery_tag)


connection = connect_rabbitmq()

channel = connection.channel()

channel.queue_declare(queue=QUEUE_NAME, durable=True)

channel.basic_consume(
    queue=QUEUE_NAME,
    on_message_callback=callback
)

print("Aguardando mensagens...")

channel.start_consuming()
