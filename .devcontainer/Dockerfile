ARG NODE_VERSION=16.0.0
ARG PYTHON_VERSION=3.9.16


FROM node:${NODE_VERSION}-alpine AS node
FROM python:${PYTHON_VERSION}-alpine AS python
FROM qmcgaw/reactdevcontainer
COPY --from=node /usr/lib /usr/lib
COPY --from=node /usr/local/share /usr/local/share
COPY --from=node /usr/local/lib /usr/local/lib
COPY --from=node /usr/local/include /usr/local/include
COPY --from=node /usr/local/bin /usr/local/bin
RUN node -v

COPY --from=python /usr/local/bin/python /usr/local/bin/python
COPY --from=python /usr/local/include/python3.9 /usr/local/include/python3.9
COPY --from=python /usr/local/lib/python3.9 /usr/local/lib/python3.9
COPY --from=python /usr/local/lib/libpython3.9.so /usr/local/lib/libpython3.9.so
COPY --from=python /usr/local/lib/libpython3.9.so.1.0 /usr/local/lib/libpython3.9.so.1.0
RUN python --version
RUN node -v
