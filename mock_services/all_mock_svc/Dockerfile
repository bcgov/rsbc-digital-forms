FROM python:3.12-alpine
ARG APP_ROOT

COPY requirements.txt ${APP_ROOT}/src/

RUN pip install -U pip setuptools wheel && \
    sha256sum "${APP_ROOT}/src/requirements.txt" > ${APP_ROOT}/requirements.sha256  && \
    cd ${APP_ROOT}/src && pip install -r requirements.txt

COPY . ${APP_ROOT}/src/mock_services/icbc_mock_svc
WORKDIR ${APP_ROOT}/src/mock_services/icbc_mock_svc

# CMD [ "gunicorn", "--error-logfile", "-", "--bind", "0.0.0.0:5000", "--pythonpath", "python/icbc_mock_svc", "wsgi" ]
CMD [ "gunicorn", "--error-logfile", "-", "--bind", "0.0.0.0:5000", "wsgi" ]

