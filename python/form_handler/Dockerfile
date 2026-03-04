FROM artifacts.developer.gov.bc.ca/redhat-docker-virtual/ubi9/python-312
ARG VERSION
ENV VERSION=$VERSION

COPY form_handler/requirements.txt ${APP_ROOT}/src/

RUN pip install -U pip setuptools && \
    sha256sum "${APP_ROOT}/src/requirements.txt" > ${APP_ROOT}/requirements.sha256  && \
    cd ${APP_ROOT}/src && pip install -r requirements.txt


COPY __init__.py ${APP_ROOT}/src/python/
COPY common ${APP_ROOT}/src/python/common
COPY form_handler ${APP_ROOT}/src/python/form_handler

# RUN ["python", "-m", "pytest", "backend/form_handler"]

CMD [ "python", "python/form_handler/listener.py" ]
