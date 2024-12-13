# API KTP Borwita

[![Docker Image](https://github.com/Capstone-Borwita/cloud-computing-path/actions/workflows/docker-image.yaml/badge.svg)](https://github.com/Capstone-Borwita/cloud-computing-path/actions)

[![Tests](https://github.com/Capstone-Borwita/cloud-computing-path/actions/workflows/bruno.yaml/badge.svg)](https://github.com/Capstone-Borwita/cloud-computing-path/actions)

This API is designed to power the mobile applications, enabling seamless integration of machine learning capabilities and backend functionalities. The API's primary responsibility is to perform machine learning tasks, including scanning KTP images to extract key data such as NIK, Name, and Address. Additionally, the API supports CRUD operations for managing stores and news.

**Key Features**:

- **Machine Learning Models**: Scans KTP images and extracts data (NIK, Name, Address)
- **CRUD Operations**: Allows the management of store and news data
- **Authentication**: Ensure Authorized Access
- **Mobile Integration**: Serves as the backend for mobile applications

For live documentation, please visit the [official docs](https://borwita-ktp-api.ignorelist.com/redoc).

**Related Repositories**:

- [Machine Learning Repository](https://github.com/Capstone-Borwita/machine-learning-path)
- [Mobile Application Repository](https://github.com/Capstone-Borwita/mobile-development-path)

---

## Requirements

- [Poetry](https://python-poetry.org/docs/#installation) (for Local Development)
- [Docker](https://docs.docker.com/get-started/get-docker/)

## Server Specifications

- RAM Usage: 1.5GB
- Storage: 15GB

## Technology Stack

- **Programming Language**: Python 3.12
- **Framework**: FastAPI
- **Database**: SQLite
- **Key Libraries**:
  - Pydantic Settings
  - SQL Model
  - Pydantic
  - Ultralytics (ML)
  - Imutils (ML)
  - Opencv Python Headless (ML)
  - Tensorflow (ML)

---

## Docker Hub

To quickly get a running instance, use Docker:

```sh
docker pull capstoneborwitac242ak01/borwita-ktp-api:latest

# For Windows, use PowerShell
echo "services:
  app:
    image: capstoneborwitac242ak01/borwita-ktp-api:latest
    volumes:
      - ./images/ml:/src/images/ml
      - ./images/user-content:/src/images/user-content
      - ./data:/src/data
    ports:
      - \"8000:8000\"
    environment:
      - MODE=production
      - TOKEN_LENGTH=64
      - ORIGIN=http://localhost:8000" > compose.yaml

docker compose up -d
```

---

## Local Installation

Clone the repository and its submodules:

```sh
git clone --recurse-submodules https://github.com/Capstone-Borwita/cloud-computing-path borwita-api
```

## Run Local Development Server

Install dependencies and run the development server:

```sh
poetry install
poetry run dev
```

## Build Docker Image

Build the Docker image locally:

```sh
docker compose build
```

## Run Docker Image

Run the Docker container:

```sh
docker compose up
```
