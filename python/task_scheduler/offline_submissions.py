import logging

from python.task_scheduler.config import Config
from python.task_scheduler.dbfuncs import query_pending_offline_submissions, update_offline_submission_status
from python.task_scheduler.eventqueuefuncs import add_to_event_queue
from python.task_scheduler.rabbitmq import RabbitMQ

def process_offline_submission(app, db):
    logging.debug("Processing offline submission...")
    try:
        queue_name = Config.OFFLINE_SUBMISSION_WATCH_QUEUE
        statusval, errmsg, all_pending_submissions = query_pending_offline_submissions(app, db)
        if statusval:
            writer = RabbitMQ(Config())
            for submission in all_pending_submissions:
                logging.verbose(submission)
                try:
                    statusval1, errmsg = add_to_event_queue(app, writer, submission, queue_name)
                    if not statusval1:
                        logging.error(errmsg)
                        continue
                    else:
                        logging.info(
                            f"offline_submission_id: {submission['id']}"
                        )
                        update_status, update_err = update_offline_submission_status(
                            app, db, submission['id'], 'processed'
                        )
                        if not update_status:
                            logging.error(
                                f"offline_submission_id: {submission['id']}"
                            )
                            raise Exception(update_err)
                except Exception as e:
                    logging.error(e)
                    continue
        elif errmsg == "No pending offline submissions found":
            logging.info(errmsg)
            return True
        else:
            raise Exception(errmsg)
    except Exception as e:
        logging.error(e)
        return False    
