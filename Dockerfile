FROM python:3.12-slim AS builder

RUN pip install poetry==1.8.4

ENV POETRY_NO_INTERACTION=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /src

COPY pyproject.toml poetry.lock ./

RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry export -f requirements.txt --without-hashes -o requirements.txt

FROM python:3.12-slim AS runtime

WORKDIR /src

RUN mkdir data

COPY --from=builder /src/requirements.txt /src/requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip pip install --no-cache-dir -r requirements.txt

COPY images ./images
COPY modules ./modules
COPY app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]
