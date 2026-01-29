FROM python:latest

WORKDIR /app

ENV PYTHONDONTWRITTEBYTEOCDE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/src

COPY pyproject.toml poetry.lock* ./

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --only main --no-root --no-interaction --no-ansi

COPY src /app/src

# TODO edit for production
CMD ["uvicorn", "securetext.main:app", "--host", "0.0.0.0", "--port", "8000"]