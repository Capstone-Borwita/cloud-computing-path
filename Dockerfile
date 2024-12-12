FROM python:3.12-slim

RUN pip install poetry==1.8.4

ENV POETRY_NO_INTERACTION=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /src

COPY pyproject.toml poetry.lock ./

RUN mkdir data
RUN touch README.md
RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

COPY images ./images
COPY modules ./modules
COPY app ./app

RUN poetry install

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0"]
