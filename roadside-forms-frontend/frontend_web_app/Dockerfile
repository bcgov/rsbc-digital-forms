# FROM registry.access.redhat.com/ubi8/nodejs-16-minimal:latest AS build
FROM artifacts.developer.gov.bc.ca/dbe7-images/node16:1.0 AS build
ARG REACT_APP_KEYCLOAK_URL
ARG REACT_APP_KEYCLOAK_REALM
ARG REACT_APP_KEYCLOAK_CLIENT_ID
ARG REACT_APP_BASE_URL
ARG PUBLIC_URL

ENV REACT_APP_KEYCLOAK_URL=$REACT_APP_KEYCLOAK_URL
ENV REACT_APP_KEYCLOAK_REALM=$REACT_APP_KEYCLOAK_REALM
ENV REACT_APP_KEYCLOAK_CLIENT_ID=$REACT_APP_KEYCLOAK_CLIENT_ID
ENV REACT_APP_BASE_URL=$REACT_APP_BASE_URL
ENV PUBLIC_URL=$PUBLIC_URL
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN ls -a

RUN npm run build
RUN ls -l





FROM artifacts.developer.gov.bc.ca/dbe7-images/ubi8-nginx120:1.0
ARG VERSION
ENV VERSION=$VERSION
COPY nginx.conf /app/nginx.conf
WORKDIR /app
COPY --from=build /app/build /app/build
# COPY dist /app/dist

CMD ["nginx", "-c", "/app/nginx.conf",  "-g", "daemon off;"]
