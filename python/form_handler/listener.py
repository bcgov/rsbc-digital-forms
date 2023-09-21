from python.form_handler.config import Config
import python.common.helper as helper
import python.form_handler.business as business
from python.form_handler.helper import middle_logic, get_listeners
from python.common.rabbitmq import RabbitMQ
from python.common.message import decode_message
import logging
import logging.config
import json
import pika

from python.form_handler.helper import get_storage_ref_event_type

from flask_api import FlaskAPI
from python.prohibition_web_svc.models import db
# from form_handler.config import Config
# import common.helper as helper
# import form_handler.business as business
# from common.rabbitmq import RabbitMQ
# from common.message import decode_message

logging.config.dictConfig(Config.LOGGING)

application = FlaskAPI(__name__)
application.config['SECRET_KEY'] = Config.FLASK_SECRET_KEY
application.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URI
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config["SQLALCHEMY_ECHO"] = False

db.init_app(application)


class Listener:
    """
        This listener watches the RabbitMQ WATCH_QUEUE defined in the
        Config.  When a message appears in the queue the Listener:
         - invokes callback(),
         - invokes middleware to determine the appropriate event
    """
    def __init__(self, config, rabbit_writer, rabbit_listener):
        self.config = config
        self.listener = rabbit_listener
        self.writer = rabbit_writer
        logging.warning('*** form verifier initialized  ***')

    def main(self):
        """
            Start listening for messages on the WATCH_QUEUE
            when a message arrives invoke the callback()
        """
        self.listener.consume(self.config.STORAGE_WATCH_QUEUE, self.callback)

    def callback(self, ch, method, properties, body):
        # convert body (in bytes) to string
        message_dict = decode_message(body, self.config.ENCRYPT_KEY)
        # TODO: Get event type by querying db
        message_dict['event_type'] = get_storage_ref_event_type(message_dict,application,db,Config.EVENT_TYPES)
        logging.info('event type: {}'.format(message_dict['event_type']))
        # message_dict['event_type'] = 'vi_form'
        # TODO: Pass event type and event to middle logic

        logging.info("callback() invoked: {}".format(json.dumps(message_dict)))
        helper.middle_logic(helper.get_listeners(business.process_incoming_form(), message_dict['event_type']),
                            message=message_dict,
                            config=self.config,
                            writer=self.writer,
                            app=application,
                            db=db)

        # Regardless of whether the process above follows the happy path or not,
        # we need to acknowledge receipt of the message to RabbitMQ below. This
        # acknowledgement deletes it from the queue. The logic above
        # must have saved / handled the message before we get here.

        ch.basic_ack(delivery_tag=method.delivery_tag)

# def create_app():
#     with application.app_context():
#         logging.warning('inside create_app()')
#         initialize_app(application)
#         return application

class DFListener:
    def __init__(self):
        hostname='amqp://admin:password@rabbitmq:5672'
        print('changed1')
        print(' [*] Connecting to rabbitmq on {}'.format(hostname))
        credentials = pika.PlainCredentials('admin', 'password')
        connection = pika.BlockingConnection(pika.ConnectionParameters(
                host='host.docker.internal',port=5672,credentials=credentials))
        channel = connection.channel()
        channel.exchange_declare(exchange='amq.direct', exchange_type='direct', durable=True)
        # result = channel.queue_declare(exclusive=False, queue='dfevents', durable=True)
        # queue_name = result.method.queue
        channel.queue_bind(exchange='amq.direct',queue='df-storage-events')      
        channel.basic_qos(prefetch_count=1)
        print('this is the queue name: {}'.format('dfevents'))
        channel.basic_consume(on_message_callback=self.callback,queue='df-storage-events',auto_ack=False)
        # print(' [*] Waiting for logs. To exit press CTRL+C')
        # channel.start_consuming()
        self.channel=channel

    @staticmethod
    def callback(ch, method, properties, body):
        print(body)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    
    def consume(self):
        """
            Start listening for messages on the WATCH_QUEUE
            when a message arrives invoke the callback()
        """
        print(' [*] Waiting for logs. To exit press CTRL+C')
        self.channel.start_consuming()


if __name__ == "__main__":
    # DFListener().consume()
    Listener(
        Config(),
        RabbitMQ(Config()),
        RabbitMQ(Config())
    ).main()
