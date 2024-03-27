[![Lifecycle:Experimental](https://img.shields.io/badge/Lifecycle-Experimental-339999)](Redirect-URL) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=bcgov_rsbc-digital-forms&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=bcgov_rsbc-digital-forms) [![OpenSSF
Scorecard](https://api.securityscorecards.dev/projects/github.com/bcgov/rsbc-digital-forms/badge)](https://api.securityscorecards.dev/projects/github.com/bcgov/rsbc-digital-forms) [![CodeQL](https://github.com/bcgov/rsbc-digital-forms/actions/workflows/codeql.yml/badge.svg)](https://github.com/bcgov/rsbc-digital-forms/actions/workflows/codeql.yml) [![trivy-scan](https://github.com/bcgov/rsbc-digital-forms/actions/workflows/trivy-scan.yml/badge.svg?branch=main)](https://github.com/bcgov/rsbc-digital-forms/actions/workflows/trivy-scan.yml)

# RSBC Digital Forms

This repository contians all components related to Digital forms application managed by RSBC team. It is a web based application used by the RCMP and other police agencies across the province of BC to issue various forms.

### OpenShift Deployment

- See the deployment documents provided.

## Requirements

- Git
- Docker
- Docker Compose
- NodeJS
- Python 3.8

## Getting Started

- Install Requirements listed above
- Login to the BCGov image repository.

## How to Develop

Please read the following for project setup instructions.

### Setting up Local Development

#### Initializing the Project

The following steps should only need to be completed **once**. Run the following commands from the project root directory. Wait for each command to complete before running the next.

1. Create .env files for the services that have .env-sample and copy the .env-sample file contents into the respective .env file
2. run `npm install` from within the roadside-forms-frontend/frontend_web_app `package-lock.lock` to install dependencies. Any new dependencies you want to add use npm workspaces command.
3. run `npm run serve` from within the roadside-forms-frontend/frontend_web_app to host the front end locally this will allow for hot reloading. You can also choose to run the front end using the docker-compose however this will not allow for hot reloading.
4. have a terminal at the root level and run `docker-compose up --build` to build and deploy the prohibition_web_svc as well as if needed the form_handler services. However, these do not utilize hot reloading and must be re-built every time changes are made.
5. If you have model changes and need a database migration these are currently handled using alembic. First go into your config.py in the prohibition_web_svc and change the DB_HOST from `db` to `localhost`. To create the migration use a venv to install the requirements.txt locally and then from the prohibition_web_svc run `flask db migrate` and once you have checked over or modified the migration in the versions folder run `flask db upgrade` to apply the migration.
6. To seed the DB with form numbers which are required for the app to work you will need to run the flask command ` flask seed-form-numbers-for-dev`
7. Once all of this is done change your DB_HOST in the config.py from `localhost` back to `db`.
8. Then on first login you will be asked to apply for access., Once this is done you will need to go into the database and the user_role table and set the approved date to the current date. This will allow your user access to the system. If you need administrator you can create a new role with all of the same information and change the role_name from officer to administrator.

#### Restarting the Project

After initializing the project, run the following commands to restart the application.

- when the docker-compose is run all migrations currently in the folder are applied to the database so they no longer need to be manually run.
- if you have deleted the volume for the DB then you will need to step 6-8 again as well as modifying the DB_HOST in the prohibition_web_svc config.py.

#### Additional Setup

##### Notifications & Emails

- TODO: need more info

### Troubleshooting

Should anything go awry with the above commands, you may wish to isolate the failure by running individual commands.

1. Delete any existing `node_modules` in frontend-web-app.
2. Make sure that you are running the correct node version. Run `make valid` to validate your environment or `node -v` to check your version and `nvm use` to use the project version.
3. Run `npm ci` to update any dependencies.
4. Docker: Docker Desktop should be running for local development.
   - Docker errors: kill & restart the docker process in a unix environment:
   - `ps -aux | grep dockerd` to find the `DOCKER_PROCESS_ID`
   - `kill -9 DOCKER_PROCESS_ID` to end the process
   - `sudo dockerd` to restart the process

Depending on your postgres setup you may have to use `host.docker.internal`.

Once you've spun up the app you may want to manually update the approved_dt:

```
psql -U <your_user> <your_db>
UPDATE user_role
SET approved_dt = submitted_dt
WHERE 1=1;
```

### Browser Caching

If you are rebuilding often, you may encounter browser caching.

To address this, you may:

- Periodically clear the cache.
- Disable cache (available in Chrome/Chromium)
- Open an Incognito window (Chrome/Chromium)

## Architecture Diagrams

- see the architechture diagrams provided.
