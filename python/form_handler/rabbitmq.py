import logging
import logging.config
import pika
import pika.exceptions
import pika.adapters.utils.connection_workflow as workflow


class RabbitMQ:

    MaximumTriesAfterError = 5

    def __init__(self, config):
        self.amqp_connection = self._get_connection_url(config)
        self.connection = self._get_connection(self.amqp_connection)
        self.channel = self._get_channel(self.connection)
        logging.basicConfig(level=config.LOG_LEVEL, format=config.LOG_FORMAT)

    @staticmethod
    def _get_connection_url(config) -> str:
        string = "amqp://{}:{}@{}:5672/%2F?connection_attempts={}&retry_delay={}".format(
            config.RABBITMQ_USER,
            config.RABBITMQ_PASS,
            config.RABBITMQ_URL,
            config.MAX_CONNECTION_RETRIES,
            config.RETRY_DELAY
        )
        logging.debug(string)
        return string

    def consume(self, queue_name: str, callback):
        self.consume_queues({queue_name: callback})

    def consume_queues(self, queue_callbacks: dict):
        try:
            self.channel.basic_qos(prefetch_count=1)
            for queue_name, callback in queue_callbacks.items():
                self._verify_or_create(queue_name)
                self.channel.basic_consume(queue=queue_name, on_message_callback=callback)
            self.channel.start_consuming()
        except Exception as error:
            logging.error('Connection Exception - will be retried', error, exc_info=True)
        

    def publish(self, queue_name: str, payload: bytes):
        logging.info('publish to: ' + queue_name)
        self._refresh_connection(queue_name)
        for tries in range(RabbitMQ.MaximumTriesAfterError):
            try:
                self.channel.basic_publish(  
                    exchange='', 
                    routing_key=queue_name, 
                    body=payload,
                    properties=pika.BasicProperties(delivery_mode=2, content_type='application/json'),
                    mandatory=True)
                return True

            except Exception as error:
                logging.warning("Could not publish message to queue ... trying to reestablish the connection")
                self._refresh_connection(queue_name)
        
        return False

    def publish_confirmed(self, queue_name: str, payload: bytes):
        logging.info('publish with confirmation to: ' + queue_name)
        for tries in range(RabbitMQ.MaximumTriesAfterError):
            try:
                self._refresh_connection(queue_name)
                self.channel.confirm_delivery()
                self.channel.basic_publish(
                    exchange='',
                    routing_key=queue_name,
                    body=payload,
                    properties=pika.BasicProperties(
                        delivery_mode=2,
                        content_type='application/json',
                    ),
                    mandatory=True,
                )
                return True
            except Exception:
                logging.warning(
                    'Could not publish confirmed message ... trying to reestablish the connection'
                )
                self._refresh_connection(queue_name)
        return False

    def _refresh_connection(self, queue_name):
        self.connection = self._get_connection(self.amqp_connection)
        self.channel = self._get_channel(self.connection)
        self.channel.queue_declare(queue=queue_name, durable=True)

    def _verify_or_create(self, queue_name: str):
       
        logging.info('verify or create: ' + queue_name)
        for tries in range(RabbitMQ.MaximumTriesAfterError):
            try:
                self.channel.queue_declare(queue=queue_name, durable=True)
                logging.info('Confirmed, there is a queue called: ' + queue_name)
                return True

            except Exception as error:
                logging.warning("Could not declare queue ... trying to reestablish the connection")
                self.connection = self._get_connection(self.amqp_connection)
                self.channel = self._get_channel(self.connection)
        
        return False

    @staticmethod
    def _get_connection(connection_url):
        logging.info('getting connection to RabbitMQ')
        parameters = pika.URLParameters(connection_url)
        return pika.BlockingConnection(parameters)

    @staticmethod
    def _get_channel(connection):
        logging.info('getting channel to RabbitMQ')
        return connection.channel()
