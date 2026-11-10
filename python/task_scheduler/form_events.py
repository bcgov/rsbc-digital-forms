import logging

from python.task_scheduler.config import Config
from python.task_scheduler.dbfuncs import query_pending_events, update_event_status
from python.task_scheduler.eventqueuefuncs import add_to_event_queue
from python.task_scheduler.rabbitmq import RabbitMQ


def process_pending_events(app, db):
    logging.verbose("process_pending_events() invoked")
    try:
        queue_name = Config.STORAGE_WATCH_QUEUE
        statusval, errmsg, all_events = query_pending_events(app, db)
        if statusval:
            writer = RabbitMQ(Config())
            for event in all_events:
                logging.debug(event)
                try:
                    statusval1, errmsg = add_to_event_queue(app, writer, event, queue_name)
                    if not statusval1:
                        logging.error(errmsg)
                        continue
                    else:
                        logging.info(
                            f"Updating processed event status for submission_id: {event['submission_id']}, "
                            f"event_id: {event['event_id']}"
                        )
                        update_status, update_err = update_event_status(
                            app, db, event['submission_id'], event['event_id'], 'processed'
                        )
                        if not update_status:
                            logging.error(
                                f"Error in updating event status for submission_id: {event['submission_id']}, "
                                f"event_id: {event['event_id']}"
                            )
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
