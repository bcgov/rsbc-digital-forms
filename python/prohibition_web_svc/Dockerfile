FROM artifacts.developer.gov.bc.ca/dbe7-images/rhel8-python39:1-196.1725368453
ARG VERSION
ENV VERSION=$VERSION

COPY prohibition_web_svc/requirements.txt ${APP_ROOT}/src/

RUN pip install --upgrade pip
RUN source /opt/app-root/etc/scl_enable && \
    set -x && \
    pip3 install -U pip setuptools wheel && \
    sha256sum "${APP_ROOT}/src/requirements.txt" > ${APP_ROOT}/requirements.sha256  && \
    cd ${APP_ROOT}/src && pip3 install -r requirements.txt

COPY __init__.py ${APP_ROOT}/src/python/
COPY common ${APP_ROOT}/src/python/common
COPY prohibition_web_svc ${APP_ROOT}/src/python/prohibition_web_svc

# RUN ["python", "-m", "pytest", "python/prohibition_web_svc"]

CMD [ "gunicorn", "--error-logfile", "-", "--bind", "0.0.0.0:5000", "--pythonpath", "python/prohibition_web_svc", "app:create_app()" ]