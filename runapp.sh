#!/bin/bash

# Activate the virtual environment (if using venv)
# source venv/bin/activate

# Start Redis (assuming it's installed and in PATH)
redis-server &

# Start Celery worker
celery -A celery_app worker --loglevel=info &

# Start the Celery app
python celery_app.py