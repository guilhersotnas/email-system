from flask import Flask, request, jsonify
import pika
import json

app = Flask(__name__)

RABBITMQ_HOST = "rabbitmq"
QUEUE_NAME = "emails"

@app.route('/send', methods=['POST'])
def send_email():

    data = request.json

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBITMQ_HOST)
    )

    channel = connection.channel()

    channel.queue_declare(
        queue=QUEUE_NAME,
        durable=True
    )

    channel.basic_publish(
        exchange='',
        routing_key=QUEUE_NAME,
        body=json.dumps(data)
    )

    connection.close()

    return jsonify({
        "message": "Email enviado para fila!"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
