[![Build and Push Docker Image](https://github.com/nogibjj/Wenye_Li_Mini_Project_12/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Wenye_Li_Mini_Project_12/actions/workflows/cicd.yml)

## Wenye Li Mini Project 12

## Requirements

Create a simple python application containerized with a dockerfile. The goal here is to both demonstrate running your application within a docker container (using docker run terminal commands) but to also build a docker image in your CI/CD pipeline which will be pushed to Docker Hub or other container management service.

## Application

A simple shopping list application built with Flask and containerized with Docker.

## Features

- Add items to shopping list
- Remove items from shopping list
- Docker containerization
- CI/CD pipeline with GitHub Actions
- Automated deployment to Docker Hub

## Local Setup

1. Clone the repository:

```bash
git clone https://github.com/nogibjj/Wenye_Li_Mini_Project_12.git
cd Wenye_Li_Mini_Project_12
```

2. Create and activate virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
make install
```

4. Run locally:

```bash
make run-local
```

## Docker Usage

1. Build image:

```bash
make build
```

2. Run container:

```bash
make run
```

3. View running containers:

```bash
make container_show
```

4. Stop container:

```bash
make stop
```

5. Clean up:

```bash
make clean
```

## CI/CD Pipeline

This project uses GitHub Actions for CI/CD:

- Automatically builds Docker image
- Pushes to Docker Hub
- Triggered on push to main branch

## Docker Hub

The Docker image is available at:

```
docker pull wenyeli/shopping-list-app:latest
```

## Commands

- `make install`: Install dependencies
- `make run-local`: Run app locally
- `make build`: Build Docker image
- `make run`: Run Docker container
- `make stop`: Stop container
- `make clean`: Clean up resources
- `make check-port`: Check port usage
