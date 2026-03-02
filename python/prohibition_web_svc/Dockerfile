FROM artifacts.developer.gov.bc.ca/redhat-docker-virtual/ubi9/python-312
ARG VERSION
ENV VERSION=$VERSION

COPY prohibition_web_svc/requirements.txt ${APP_ROOT}/src/

RUN pip3 install -U pip setuptools wheel && \
    sha256sum "${APP_ROOT}/src/requirements.txt" > ${APP_ROOT}/requirements.sha256  && \
    cd ${APP_ROOT}/src && pip3 install -r requirements.txt

# Switch to root user for system package installation
USER root

# Install system dependencies for Playwright
RUN yum update -y && \
    yum install -y \
    glib2-devel \
    nss \
    nspr \
    atk \
    at-spi2-atk \
    cups-libs \
    libdrm \
    gtk3 \
    libXcomposite \
    libXdamage \
    libXrandr \
    mesa-libgbm \
    libXScrnSaver \
    alsa-lib \
    liberation-fonts-common \
    dejavu-sans-fonts \
    dejavu-serif-fonts \
    dejavu-sans-mono-fonts \
    && yum clean all

# Switch back to the default user
USER 1001

# Install Playwright browsers
RUN playwright install chromium

# Install Playwright system dependencies (skip problematic fonts)
RUN playwright install-deps chromium || true

COPY __init__.py ${APP_ROOT}/src/python/
COPY common ${APP_ROOT}/src/python/common
COPY prohibition_web_svc ${APP_ROOT}/src/python/prohibition_web_svc

# RUN ["python", "-m", "pytest", "python/prohibition_web_svc"]

CMD [ "gunicorn", "--error-logfile", "-", "--bind", "0.0.0.0:5000", "--pythonpath", "python/prohibition_web_svc", "app:create_app()" ]