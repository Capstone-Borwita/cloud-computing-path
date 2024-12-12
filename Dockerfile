FROM python:3.12-slim AS builder

RUN pip install poetry==1.8.4

ENV POETRY_NO_INTERACTION=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /src

COPY pyproject.toml poetry.lock ./

# poetry engga support install dari source khusus
# jadi kalo pake poetry dengan normal, terpaksa pake ultralytics dengan GPU
# jadi ultralytics bakal diinstall manual biar bisa tanpa GPU
RUN sed -i '/ultralytics/d' pyproject.toml
RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry export -f requirements.txt --without-hashes -o requirements.txt

FROM python:3.12-slim AS runtime

# install dependency ultralytics
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 libglib2.0-0 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /src

RUN mkdir data

COPY --from=builder /src/requirements.txt /src/requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip pip install --no-cache-dir -r requirements.txt

# install ultralytics (tanpa GPU)
RUN --mount=type=cache,target=/root/.cache/pip pip install --no-cache-dir torch==2.3.1+cpu torchvision==0.18.1+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html && pip install --no-cache-dir ultralytics==8.0.200

COPY images ./images
COPY modules ./modules
COPY app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]
