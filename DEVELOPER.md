# RSBC Digital Forms (road-side forms) development

Project information for developers and testers. This project is for the road-side forms that police fill out when a driver receives a 12-hour driving suspension, 24-hour driving prohibition, or vehicular impoundment.


## Resources

- [Jira project dashboard](https://justice.gov.bc.ca/jirarsi/secure/RapidBoard.jspa?rapidView=1082&quickFilter=2003&quickFilter=4341)
- [Confluence project](https://justice.gov.bc.ca/wiki/display/RDFP/RSBC+Digital+Forms+Project+Home) (product management and software test documentation): search this space to find management, design, development, and testing documentation. Potentially useful resources include:
  - [Business artefacts (police forms and feedback)](https://justice.gov.bc.ca/wiki/display/RDFP/Business+Artifacts+and+Documents) and [process models](https://justice.gov.bc.ca/wiki/display/RDFP/Business+Process+Models)
  - [Business requirements](https://justice.gov.bc.ca/wiki/display/RDFP/DF+Business+Requirements)
  - [Technical architecture](https://justice.gov.bc.ca/wiki/display/RDFP/Technical+Architecture)
  - [Technical testing and reverse-engineering, broken down by project](https://justice.gov.bc.ca/wiki/display/RDFP/Digital+Forms+project+testing)
- [Teams/SharePoint documents](https://bcgov.sharepoint.com/teams/01606/Shared%20Documents/Forms/AllItems.aspx?csf=1&web=1&e=zlzA3Y&cid=5a962a27-9e86-4fbe-b29b-1ee2b78ad987&FolderCTID=0x012000ECAA2FC3493BAC4BB0BF800B23569AF3&id=/teams/01606/Shared%20Documents/DF%20Application%20Development&viewid=ed110e6a-fbb2-4ee5-9752-91b3496db49e) (application development documentation)
- [GitHub repo](https://github.com/bcgov/rsbc-digital-forms/) (source code)
- [OpenShift project (licence plate 'be78d6')](https://console.apps.silver.devops.gov.bc.ca/k8s/cluster/project.openshift.io~v1~Project) environments:
    - [DEV](https://console.apps.silver.devops.gov.bc.ca/k8s/ns/be78d6-dev/core~v1~Service)
    - [TEST](https://console.apps.silver.devops.gov.bc.ca/k8s/ns/be78d6-test/core~v1~Service)
    - [PROD](https://console.apps.silver.devops.gov.bc.ca/k8s/ns/be78d6-prod/core~v1~Service)


## Set up a local development environment

These steps walk you through creating your own local development environment on Windows 10. The process will be similar for Mac or Linux. If you are using a Mac or Linux system to set up a development environment, please document any extra steps you needed to get up and running, then update this message to say that you tested the steps on your platform.


### Requirements

You need the following tools installed before you can create a development environment. In August 2023, these were the versions available:

- **git** --version > git version 2.40.1.windows.1
- **node** --version > v18.16.0
- **npm** --version > 9.6.7
- **python** --version > Python 3.10.6
- **pip** --version > pip 22.3 from C:\Python310\lib\site-packages\pip (python 3.10)
- **choco** --version > 1.1.0
- **Docker Desktop**, which requires Hyper-V to be installed. Hyper-V requires a CPU with hardware virtualization and a non-Home edition of Windows (e.g. Windows Pro or Enterprise edition). You may be able to use the standard Docker on Windows Home editions with WSL2 and no Hyper-V, but that configuration has not been tested.

The typical integrated development environment used on this project is Visual Studio Code.


### Installing Docker Desktop

To install Docker Desktop with Chocolatey, run the following command from an elevated command prompt:

    choco install docker-desktop docker-cli docker-compose

Docker Desktop will appear on  the Start menu, but you need to log in and out to start the services before using it. Also, docker-compose and docker.exe will be on your path. In August 2023, these were the versions used:

- **Docker Desktop** version 4.21.0, which included:
  - **docker** --version > 24.0.2, build cb74dfc
  - **docker-compose** --version > v2.19.1


### Access to Artifactory

Once Docker is installed, you must log in to the container registry from Docker. The container images are stored in an OpenShift Artifactory repository. The command to log in is shown below. You can obtain a working credential from a member of the development team and replace the words "USERNAME" and "PASSWORD" below:

    docker login --username USERNAME --password PASSWORD artifacts.developer.gov.bc.ca/dbe7-images


### Using Docker Compose

Once you have the tools installed, you can use Docker Compose to build the server images, deploy the checked out code, and start the servers.

The development environment runs in several Docker containers, described in *docker-compose.yaml*:

| # | Component         | Container name     | Description                     |
|---|-------------------|--------------------|---------------------------------|
| 1 | Backend database  | db                 | Postgres database on port 5432  |
| 2 | Backend API       | roadside-forms-api | REST API server on port 5000    |
| 3 | Front end web app | web_app            | Web server on port 5000         |
| 4 | Form handler      | form_handler       | Currently not used              |
| 5 | RabbitMQ          | rabbitmq           | Currently not used              |

**NOTE**: The `web_app` section of *docker-compose.yaml* in git is commented out. To run a full development environment, you must uncomment all the lines for the `web_app` section before starting using the `docker-compose` command. However, you may wish to leave the web_app section commented out if you plan to run the web app outside of a container.

The *docker-compose.yaml* file reads in variables and secrets from the `.env` file in the project root. This file is not checked in to git, but you can get a working copy from another member of the development team. You can see the template for `.env` in `.env.sample`.


#### Start the containers

This command starts the container. If the containers have not yet been built, they are built first:

    docker-compose up

To rebuild the containers after an update:

    docker-compose up --build

To pull fresh containers and rebuild everything from scratch:

	docker-compose up --build --force-recreate

To see running containers, use Docker Desktop or:

    docker ps


#### Docker examples

Here is an example of the output from the `docker-compose up` command where all three containers are started:
```
$ docker-compose up
[+] Running 4/4
 ✔ Network rsf-app_docker-network          Created                                                                                                                                                            0.0s
 ✔ Container rsf-app-db-1                  Created                                                                                                                                                            0.0s
 ✔ Container rsf-app-roadside-forms-api-1  Created                                                                                                                                                            0.0s
 ✔ Container rsf-app-web_app-1             Created                                                                                                                                                            0.0s

Attaching to rsf-app-db-1, rsf-app-roadside-forms-api-1, rsf-app-web_app-1
rsf-app-db-1                  |
rsf-app-db-1                  | PostgreSQL Database directory appears to contain a database; Skipping initialization
rsf-app-db-1                  |
rsf-app-db-1                  |
rsf-app-db-1                  | 2023-08-11 20:17:54.863 UTC [1] LOG:  starting PostgreSQL 14.1 on x86_64-pc-linux-musl, compiled by gcc (Alpine 10.3.1_git20211027) 10.3.1 20211027, 64-bit
rsf-app-db-1                  | 2023-08-11 20:17:54.863 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
rsf-app-db-1                  | 2023-08-11 20:17:54.863 UTC [1] LOG:  listening on IPv6 address "::", port 5432
rsf-app-db-1                  | 2023-08-11 20:17:54.867 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
rsf-app-db-1                  | 2023-08-11 20:17:54.872 UTC [21] LOG:  database system was shut down at 2023-08-11 18:50:55 UTC
rsf-app-db-1                  | 2023-08-11 20:17:54.875 UTC [1] LOG:  database system is ready to accept connections
rsf-app-web_app-1             | /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
rsf-app-web_app-1             | /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
rsf-app-web_app-1             | /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
rsf-app-web_app-1             | 10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
rsf-app-web_app-1             | 10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
rsf-app-web_app-1             | /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
rsf-app-web_app-1             | /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
rsf-app-web_app-1             | /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
rsf-app-web_app-1             | /docker-entrypoint.sh: Configuration complete; ready for start up
rsf-app-roadside-forms-api-1  | 2023-08-11 20:18:01,103::INFO::root::*** static blueprint loaded ***
rsf-app-roadside-forms-api-1  | 2023-08-11 20:18:01,161::INFO::root::*** forms blueprint loaded ***
rsf-app-roadside-forms-api-1  | 2023-08-11 20:18:01,162::INFO::root::*** admin/forms blueprint loaded ***
rsf-app-roadside-forms-api-1  | 2023-08-11 20:18:01,164::INFO::root::*** icbc blueprint loaded ***
rsf-app-roadside-forms-api-1  | 2023-08-11 20:18:01,165::INFO::root::*** user_roles blueprint loaded ***
rsf-app-roadside-forms-api-1  | 2023-08-11 20:18:01,166::INFO::root::*** admin/users_roles blueprint loaded ***
rsf-app-roadside-forms-api-1  | 2023-08-11 20:18:01,167::INFO::root::*** admin/users blueprint loaded ***
rsf-app-roadside-forms-api-1  | 2023-08-11 20:18:01,168::INFO::root::*** users blueprint loaded ***
rsf-app-roadside-forms-api-1  | INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
rsf-app-roadside-forms-api-1  | INFO  [alembic.runtime.migration] Will assume transactional DDL.
rsf-app-roadside-forms-api-1  | [2023-08-11 20:18:01 +0000] [1] [INFO] Starting gunicorn 20.1.0
rsf-app-roadside-forms-api-1  | [2023-08-11 20:18:01 +0000] [1] [INFO] Listening at: http://0.0.0.0:5000 (1)
rsf-app-roadside-forms-api-1  | [2023-08-11 20:18:01 +0000] [1] [INFO] Using worker: sync
rsf-app-roadside-forms-api-1  | [2023-08-11 20:18:01 +0000] [10] [INFO] Booting worker with pid: 10
rsf-app-roadside-forms-api-1  | 2023-08-11 20:18:01,790::INFO::root::*** static blueprint loaded ***
rsf-app-roadside-forms-api-1  | 2023-08-11 20:18:01,798::INFO::root::*** forms blueprint loaded ***
rsf-app-roadside-forms-api-1  | 2023-08-11 20:18:01,799::INFO::root::*** admin/forms blueprint loaded ***
rsf-app-roadside-forms-api-1  | 2023-08-11 20:18:01,801::INFO::root::*** icbc blueprint loaded ***
rsf-app-roadside-forms-api-1  | 2023-08-11 20:18:01,803::INFO::root::*** user_roles blueprint loaded ***
rsf-app-roadside-forms-api-1  | 2023-08-11 20:18:01,804::INFO::root::*** admin/users_roles blueprint loaded ***
rsf-app-roadside-forms-api-1  | 2023-08-11 20:18:01,805::INFO::root::*** admin/users blueprint loaded ***
rsf-app-roadside-forms-api-1  | 2023-08-11 20:18:01,807::INFO::root::*** users blueprint loaded ***
rsf-app-roadside-forms-api-1  | 2023-08-11 20:18:01,836::WARNING::root::inside create_app()
```

Here is an example of output from the `docker ps` command when the containers are running:

```
CONTAINER ID  IMAGE                       COMMAND                 CREATED        STATUS                  PORTS                              NAMES
be2602a8a2f4  rsf-app-web_app             "/docker-entrypoint.…"  5 minutes ago  Up 5 minutes            80/tcp, 0.0.0.0:8080->5000/tcp    rsf-app-web_app-1
ab04830e0799  rsf-app-roadside-forms-api  "container-entrypoin…"  5 minutes ago  Up 5 minutes            8080/tcp, 0.0.0.0:5002->5000/tcp  rsf-app-roadside-forms-api-1
beb173ab8478  postgres:14.1-alpine        "docker-entrypoint.s…"  5 minutes ago  Up 5 minutes (healthy)  0.0.0.0:5432->5432/tcp            rsf-app-db-1
```

### Access

Once running with the default configuration, you can go to:

- Web app: http://127.0.0.1:8080
- REST API: http://127.0.0.1:5000 
- Postgres database: 127.0.0.1:5432


### Running the web app locally

You may wish to run the web app locally, instead of inside a container. This may make debugging easier and faster, with fewer resources. If you do this, make sure the `web_app` section of *docker-compose.yaml* is commented out. The web app project is in the folder `.\roadside-forms-frontend\frontend_web_app`.

**Tip**: Be aware that the `npm install` command will put the NodeJS libraries and dependencies into a `node_modules` folder, which will grow to over gigabyte in size, with over a hundred thousand files. This may impact your folder searches and backup process. There is an entry in .gitignore for this folder, so the folder should not get accidentally added to git.