# FROM python:3.9.18
FROM artifacts.developer.gov.bc.ca/dbe7-images/rhel8-python39:1-196.1725368453
RUN [ "pwd" ]
RUN [ "ls", "-R" ]

COPY requirements.txt ${APP_ROOT}/src/
CMD [ "echo" , "requirements copied" ]

RUN source /opt/app-root/etc/scl_enable && \
    set -x && \
    pip install -U pip setuptools wheel && \
    sha256sum "${APP_ROOT}/src/requirements.txt" > ${APP_ROOT}/requirements.sha256  && \
    cd ${APP_ROOT}/src && pip install -r requirements.txt

CMD [ "echo" , "requirements installed" ]
RUN [ "pwd" ]
RUN [ "ls", "-R" ]

COPY . ${APP_ROOT}/src/mock_services/icbc_mock_svc

WORKDIR ${APP_ROOT}/src/mock_services/icbc_mock_svc

CMD [ "echo" , "python files copied" ]
RUN [ "pwd" ]
RUN [ "ls", "-R" ]

# CMD [ "gunicorn", "--error-logfile", "-", "--bind", "0.0.0.0:5000", "--pythonpath", "python/icbc_mock_svc", "wsgi" ]
CMD [ "gunicorn", "--error-logfile", "-", "--bind", "0.0.0.0:5000", "wsgi" ]

