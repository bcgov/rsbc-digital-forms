FROM artifacts.developer.gov.bc.ca/dbe7-images/rhel8-python36-1:1.0
ARG VERSION
ENV VERSION=$VERSION

COPY prohibition_web_svc/requirements.txt ${APP_ROOT}/src/

RUN source /opt/app-root/etc/scl_enable && \
    set -x && \
    pip install -U pip setuptools wheel && \
    sha256sum "${APP_ROOT}/src/requirements.txt" > ${APP_ROOT}/requirements.sha256  && \
    cd ${APP_ROOT}/src && pip install -r requirements.txt

COPY __init__.py ${APP_ROOT}/src/backend/
COPY common ${APP_ROOT}/src/backend/common
COPY prohibition_web_svc ${APP_ROOT}/src/backend/prohibition_web_svc

RUN ["python", "-m", "pytest", "backend/prohibition_web_svc"]

CMD [ "gunicorn", "--error-logfile", "-", "--bind", "0.0.0.0:5000", "--pythonpath", "backend/prohibition_web_svc", "app:create_app()" ]