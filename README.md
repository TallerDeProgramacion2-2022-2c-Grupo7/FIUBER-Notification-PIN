# FIUBER-Notification-PIN

![licence](https://img.shields.io/github/license/TallerDeProgramacion2-2022-2c-Grupo7/FIUBER-BO-BE)

[![Deploy](https://github.com/TallerDeProgramacion2-2022-2c-Grupo7/FIUBER-Notification-PIN/actions/workflows/deployment.yml/badge.svg?branch=main)](https://github.com/TallerDeProgramacion2-2022-2c-Grupo7/FIUBER-Notification-PIN/actions/workflows/deployment.yml)

Backend for FIUBER's WhatsApp notification PIN.

## Local installation & usage

1. Copy the Firebase credentials JSON (`firebase_credentials.json`) into the `./` directory of the repository.

2. Create a `.env` into `./fastapi_app` where the variables `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN` and `TWILIO_PHONE_NUMBER` are defined.

3. Install dependencies
```
poetry install
poetry self add poetry-dotenv-plugin
```

4. Start the server:
```
poetry run python fastapi_app/app.py
```

The API will be available on `http://localhost:8000/`.

## Repository setup & okteto deployment

The following GitHub Actions Secrets are required:
1. `DOCKERHUB_USERNAME`
2. `DOCKERHUB_TOKEN`
3. `KUBE_CONFIG_DATA` (generated with `cat kubeconfig.yaml | base64 -w 0`)
4. `TWILIO_ACCOUNT_SID`
5. `TWILIO_AUTH_TOKEN`
6. `TWILIO_PHONE_NUMBER`
7. `FIREBASE_CREDENTIALS` (generated with `cat firebase-credentials.json | base64 -w 0`)