import pika
from pika import credentials


class RabbitmqConnectionManager:

    def __init__(self):
        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost',
                                      port=5672,
                                      credentials=credentials.PlainCredentials(
                                          username="rabbit_example",
                                          password="rabbit_password_example")))
        self._exchange_name = 'exchange_name'
        self._queue_name = 'queue_name'
        self._channel = self._connection.channel()
        self._channel.exchange_declare(exchange=self._exchange_name,
                                       exchange_type='fanout')
        self._channel.queue_declare(queue=self._queue_name)
        self._channel.queue_bind(queue=self._queue_name, exchange=self._exchange_name)

    def publish(self, body):
        self._channel.basic_publish(exchange=self._exchange_name,
                                    routing_key='',
                                    body=body)

    def close(self):
        self._connection.close()
