steps:
  # Step 1: Run unit tests
  - name: 'python:3.9-slim'
    id: 'run-tests'
    entrypoint: /bin/sh
    args:
      - -c
      - |
        pip install -r requirements.txt
        cd app
        python -m unittest discover

  # Step 2: Build and push the image in one step using Google's builder
  - name: 'gcr.io/cloud-builders/gcloud'
    id: 'build-and-push'
    entrypoint: /bin/bash
    args:
      - '-c'
      - |
        gcloud builds submit --tag gcr.io/$PROJECT_ID/flask-app:latest .

  # Step 3: Deploy container image to Cloud Run
  - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
    id: 'deploy-to-cloud-run'
    entrypoint: gcloud
    args:
      - 'run'
      - 'deploy'
      - 'flask-app'
      - '--image'
      - 'gcr.io/$PROJECT_ID/flask-app:latest'
      - '--region'
      - 'us-central1'
      - '--platform'
      - 'managed'
      - '--allow-unauthenticated'

options:
  logging: 'NONE'