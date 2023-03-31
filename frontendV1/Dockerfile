# FROM registry.access.redhat.com/ubi8/nodejs-16-minimal:latest AS build
FROM artifacts.developer.gov.bc.ca/dbe7-images/ubi8-nodejs16:1.0 AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
RUN ls -l





FROM artifacts.developer.gov.bc.ca/dbe7-images/ubi8-nginx120:1.0
ARG VERSION
ENV VERSION=$VERSION
COPY nginx.conf /app/nginx.conf
WORKDIR /app
COPY --from=build /app/dist /app/dist
# COPY dist /app/dist

CMD ["nginx", "-c", "/app/nginx.conf",  "-g", "daemon off;"]