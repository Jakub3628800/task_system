FROM python:3.9

WORKDIR /app

COPY pyproject.toml .
COPY celery_app.py .
COPY tasks.py .
COPY lib/ ./lib/
COPY tests/ ./tests/

RUN pip install uv
RUN uv pip install -e .[test]

CMD ["python", "celery_app.py"]