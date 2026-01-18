FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITTEBYTEOCDE=1
ENV PYTHONUNBUFFERED=1

COPY pyproject.toml poetry.lock* ./

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --only main --no-root --no-interaction --no-ansi

COPY src /app/src

CMD ["uvicorn", "securetext.main:app", "--host", "0.0.0.0", "--port", "8001"]