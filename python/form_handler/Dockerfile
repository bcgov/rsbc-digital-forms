# FROM python:3.7.3-stretch
# FROM registry.access.redhat.com/rhscl/python-36-rhel7:latest
# FROM artifacts.developer.gov.bc.ca/dbe7-images/rhel8-python36-1:1.0
FROM artifacts.developer.gov.bc.ca/dbe7-images/rhel8-python38:1-127.1684740820
ARG VERSION
ENV VERSION=$VERSION

COPY form_handler/requirements.txt ${APP_ROOT}/src/
RUN ls -a

RUN ls /opt/app-root/etc/
RUN source /opt/app-root/etc/scl_enable && \
    set -x && \
    pip install -U pip setuptools && \
    sha256sum "${APP_ROOT}/src/requirements.txt" > ${APP_ROOT}/requirements.sha256  && \
    cd ${APP_ROOT}/src && pip install -r requirements.txt


COPY __init__.py ${APP_ROOT}/src/python/
COPY common ${APP_ROOT}/src/python/common
COPY form_handler ${APP_ROOT}/src/python/form_handler
COPY prohibition_web_svc/models.py ${APP_ROOT}/src/python/form_handler/models.py

# RUN ["python", "-m", "pytest", "backend/form_handler"]

CMD [ "python", "python/form_handler/listener.py" ]
