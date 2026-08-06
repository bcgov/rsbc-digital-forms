# RSBC Digital Forms

A BC government web application enabling **RCMP and police agencies across British Columbia** to issue digital roadside forms — replacing paper for **12-hour driving suspensions, 24-hour prohibitions, and vehicle impoundments**.

---

## Key Services

| Service | Tech | Role |
|---|---|---|
| **Frontend** | React 18, Redux, Bootstrap | Officer-facing form UI |
| **REST API** | Flask + Gunicorn | Main backend (forms, ICBC, users, files, PDFs) |
| **Form Handler** | Python + RabbitMQ | Async PDF gen, email, external API calls |
| **Task Scheduler** | Python | Cron-style background jobs |
| **PostgreSQL** | 14.1 | Primary database |
| **MinIO** | S3-compatible | PDF/file object storage |
| **Keycloak** | 26.4 | OAuth2/OIDC authentication |
| **Mock Services** | Flask | Local dev mocks (ICBC, VIPS, Comm Services) |

---

## Architecture & Data Flow

```
┌─────────────────────────────────────────────┐
│           Frontend (React)                  │
│   http://localhost:8080                     │
│   - Officer-facing form UI                  │
│   - Redux state, Dexie (IndexedDB)          │
└──────────────────┬──────────────────────────┘
                   │ API Calls
                   ▼
┌─────────────────────────────────────────────┐
│        REST API Backend (Flask)             │
│   http://localhost:5002                     │
│   Blueprints: forms, admin, icbc,           │
│   users, events, files, email, print        │
└───────────┬─────────────────┬───────────────┘
            │                 │
            ▼                 ▼
    ┌──────────────┐   ┌──────────────┐
    │  PostgreSQL  │   │    MinIO     │
    │  (port 5432) │   │  (port 9000) │
    └──────────────┘   └──────────────┘
            │
            ▼
┌─────────────────────────────────────────────┐
│         RabbitMQ (port 5672)                │
│   ├─► form_handler — PDF gen, email,        │
│   │                  ICBC/VIPS/Comm APIs    │
│   └─► task_scheduler — background jobs     │
└─────────────────────────────────────────────┘
            │
            ▼
┌─────────────────────────────────────────────┐
│         Keycloak (port 8083)                │
│   OAuth2/OIDC — auth & role management      │
└─────────────────────────────────────────────┘
```

1. Officer fills out a form in the **React frontend**
2. Form is submitted to the **Flask API** → stored in **PostgreSQL**, PDFs uploaded to **MinIO**
3. Events published to **RabbitMQ**
4. **form_handler** consumes events → generates PDFs, sends emails, calls **ICBC/VIPS** APIs
5. **task_scheduler** handles periodic retries, cleanup, and background jobs

---

## Tech Stack

### Backend (Python)
- **Framework**: Flask 2.2+ with Gunicorn
- **ORM**: Flask-SQLAlchemy + Alembic migrations
- **Messaging**: RabbitMQ with pika
- **PDF**: PyMuPDF
- **Auth**: python-keycloak
- **Testing**: pytest

### Frontend (Node.js / React)
- **Framework**: React 18.2, React Router v6
- **State**: Redux Toolkit, Recoil
- **UI**: React Bootstrap 2, Bootstrap 5
- **Forms**: Formik
- **HTTP**: Axios
- **Offline**: Dexie (IndexedDB)
- **Testing**: Jest, Cypress

### Infrastructure
- **Containers**: Docker + Docker Compose
- **Auth**: Keycloak 26.4
- **Storage**: MinIO (S3-compatible)
- **Deployment**: OpenShift (DEV/TEST/PROD, namespace `be78d6`)
- **CI/CD**: GitHub Actions

### External Integrations
- **ICBC API** — insurance/vehicle data
- **VIPS API** — vehicle impound/violation system
- **Communication Services API** — email/notification delivery

---

## Local Development

### Quick Start
```bash
cp .env.sample .env        # configure secrets
docker-compose up --build  # start all services
flask seed-form-numbers-for-dev  # seed initial data
```

### Make Commands
```bash
make build_start_common        # build and start main stack
make start_local               # start without rebuilding
make down_common               # stop main stack
make build_start_form_handler  # build form handler
make run_cron_jobs             # run cron job scheduler
```

### Service URLs

| Service | URL |
|---|---|
| Frontend | http://localhost:8080 |
| REST API | http://localhost:5002 |
| PostgreSQL | localhost:5432 |
| Keycloak | http://localhost:8083 |
| MinIO Console | http://localhost:9090 |
| RabbitMQ Web | http://localhost:15672 |
| Mock Services | http://localhost:5003 |

---

## CI/CD & Security

- **GitHub Actions** workflows for CI (lint, test, build) and CD (deploy to OpenShift)
- **SonarCloud** — code quality analysis
- **CodeQL** — static security analysis
- **Trivy** — container vulnerability scanning
- **OpenSSF Scorecard** — supply chain security
- **Alembic** — automated database migrations (`db-migrate-workflow.yml`)

---

## Project Info

- **Version**: 2.3.6
- **License**: BCGov Open Source
- **Repository**: https://github.com/bcgov/rsbc-digital-forms/
