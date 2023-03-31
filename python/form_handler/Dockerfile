# FROM python:3.7.3-stretch
# FROM registry.access.redhat.com/rhscl/python-36-rhel7:latest
FROM artifacts.developer.gov.bc.ca/dbe7-images/rhel8-python36-1:1.0
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


COPY __init__.py ${APP_ROOT}/src/backend/
COPY common ${APP_ROOT}/src/backend/common
COPY form_handler ${APP_ROOT}/src/backend/form_handler

# RUN ["python", "-m", "pytest", "backend/form_handler"]

CMD [ "python", "backend/form_handler/listener.py" ]