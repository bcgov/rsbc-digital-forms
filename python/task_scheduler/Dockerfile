FROM artifacts.developer.gov.bc.ca/dbe7-images/rhel8-python39:1-196.1725368453
ARG VERSION
ENV VERSION=$VERSION

COPY task_scheduler/requirements.txt ${APP_ROOT}/src/
RUN ls -a

RUN ls /opt/app-root/etc/
RUN source /opt/app-root/etc/scl_enable && \
    set -x && \
    pip install -U pip setuptools && \
    sha256sum "${APP_ROOT}/src/requirements.txt" > ${APP_ROOT}/requirements.sha256  && \
    cd ${APP_ROOT}/src && pip install -r requirements.txt


COPY __init__.py ${APP_ROOT}/src/python/
COPY common ${APP_ROOT}/src/python/common
COPY task_scheduler ${APP_ROOT}/src/python/task_scheduler
COPY prohibition_web_svc/models.py ${APP_ROOT}/src/python/task_scheduler/models.py

CMD [ "gunicorn", "--error-logfile", "-", "--bind", "0.0.0.0:5000", "--pythonpath", "python/task_scheduler", "main:create_app()" ]