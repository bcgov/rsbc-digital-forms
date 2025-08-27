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
    drm \
    gtk3 \
    libXcomposite \
    libXdamage \
    libXrandr \
    libgbm \
    libxss \
    alsa-lib \
    liberation-fonts \
    dejavu-fonts-common \
    && yum clean all

# Switch back to the default user
USER 1001

# Install Playwright browsers
RUN source /opt/app-root/etc/scl_enable && \
    playwright install chromium

# Install Playwright system dependencies (skip problematic fonts)
RUN source /opt/app-root/etc/scl_enable && \
    playwright install-deps chromium || true

COPY __init__.py ${APP_ROOT}/src/python/
COPY common ${APP_ROOT}/src/python/common
COPY prohibition_web_svc ${APP_ROOT}/src/python/prohibition_web_svc

# RUN ["python", "-m", "pytest", "python/prohibition_web_svc"]

CMD [ "gunicorn", "--error-logfile", "-", "--bind", "0.0.0.0:5000", "--pythonpath", "python/prohibition_web_svc", "app:create_app()" ]