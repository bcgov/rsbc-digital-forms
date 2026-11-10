from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from python.common.verbose_logging import VERBOSE_LEVEL_NUM, verbose
from python.task_scheduler.config import Config
import logging
import logging.config
from python.task_scheduler.dbfuncs import query_pending_events
from python.task_scheduler.form_events import process_pending_events
from python.task_scheduler.offline_submissions import process_offline_submission


# app = Flask(__name__)

from flask import Flask
from python.common.models import db

logging.addLevelName(VERBOSE_LEVEL_NUM, 'VERBOSE')
logging.verbose = verbose
logging.config.dictConfig(Config.LOGGING)

app = Flask(__name__)
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

def create_app():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        process_pending_events,
        'interval',
        seconds=Config.TASK_SCHEDULER_INTERVAL_SECONDS,
        args=[app, db],
    )
    scheduler.add_job(
        process_offline_submission,
        'interval',
        seconds=Config.TASK_SCHEDULER_INTERVAL_SECONDS,
        args=[app, db],
    )
    
    scheduler.start()
    return app

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        process_pending_events,
        'interval',
        seconds=Config.TASK_SCHEDULER_INTERVAL_SECONDS,
        args=[app, db],
    )
    scheduler.add_job(
        process_offline_submission,
        'interval',
        seconds=Config.TASK_SCHEDULER_INTERVAL_SECONDS,
        args=[app, db],
    )
    scheduler.start()

    # Shut down the scheduler when exiting the app
    try:
        app.run(use_reloader=False)  # use_reloader=False to prevent duplicate jobs
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()