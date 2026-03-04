FROM artifacts.developer.gov.bc.ca/redhat-docker-virtual/ubi9/python-312
ARG VERSION
ENV VERSION=$VERSION

COPY task_scheduler/requirements.txt ${APP_ROOT}/src/

RUN pip3 install -U pip "setuptools<70.0.0" wheel && \
    sha256sum "${APP_ROOT}/src/requirements.txt" > ${APP_ROOT}/requirements.sha256  && \
    cd ${APP_ROOT}/src && pip3 install -r requirements.txt

COPY __init__.py ${APP_ROOT}/src/python/
COPY common ${APP_ROOT}/src/python/common
COPY task_scheduler ${APP_ROOT}/src/python/task_scheduler

CMD [ "gunicorn", "--error-logfile", "-", "--bind", "0.0.0.0:5000", "--pythonpath", "python/task_scheduler", "main:create_app()" ]