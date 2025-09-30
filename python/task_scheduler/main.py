from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from python.common.verbose_logging import VERBOSE_LEVEL_NUM, verbose
from python.task_scheduler.config import Config
import logging
import logging.config
from python.task_scheduler.dbfuncs import query_pending_events,update_event_status
from python.task_scheduler.eventqueuefuncs import add_to_event_queue
from python.task_scheduler.rabbitmq import RabbitMQ


# app = Flask(__name__)

from flask_api import FlaskAPI
from python.common.models import db

logging.addLevelName(VERBOSE_LEVEL_NUM, 'VERBOSE')
logging.verbose = verbose
logging.config.dictConfig(Config.LOGGING)

app = FlaskAPI(__name__)
app.config['SECRET_KEY'] = Config.FLASK_SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_ECHO"] = False

db.init_app(app)

# add a ping route
@app.route('/ping', methods=['GET'])
def ping():
    return {'message': 'pong'}

def my_periodic_task():
    print("This task is running every 10 seconds.")
    query_pending_events(app,db)

def process_pending_events():
    logging.verbose("process_pending_events() invoked")
    try:        
        statusval,errmsg,all_events=query_pending_events(app,db)
        if statusval:
            writer=RabbitMQ(Config())
            for event in all_events:
                logging.debug(event)
                try:
                    statusval1, errmsg=add_to_event_queue(app, writer, event)
                    if not statusval1:
                        logging.error(errmsg)
                        continue
                    else:
                        logging.info(f"Updating processed event status for event_id: {event['event_id']}")
                        update_status,update_err=update_event_status(app,db,event['event_id'],'processed')
                        if not update_status:
                            logging.error(f"Error in updating event status for event_id: {event['event_id']}")
                            raise Exception(update_err)
                except Exception as e:
                    logging.error(e)
                    continue
        elif errmsg == "No pending events found":
            logging.info(errmsg)
            return True
        else:
            raise Exception(errmsg)
    except Exception as e:
        logging.error(e)
        return False
    
def create_app():
    scheduler = BackgroundScheduler()
    scheduler.add_job(process_pending_events, 'interval', seconds=Config.TASK_SCHEDULER_INTERVAL_SECONDS)
    scheduler.start()
    return app

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(process_pending_events, 'interval', seconds=Config.TASK_SCHEDULER_INTERVAL_SECONDS)
    scheduler.start()

    # Shut down the scheduler when exiting the app
    try:
        app.run(use_reloader=False)  # use_reloader=False to prevent duplicate jobs
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()