# Docker Learning Project

A simple Python Flask app for learning Docker concepts and best practices.

## Features

- Flask web server with JSON data
- Docker multi-stage build
- Docker Compose multi-container setup
- Volumes for persistent data
- Health checks
- Environment variables
- Exposes port 5000

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

1. Clone this repository:

```bash
git clone https://github.com/yourusername/docker-learning-project.git
cd docker-learning-project
```

2. Build and start the container using Docker Compose:

```bash
docker-compose up --build
```

3. Open your browser or use `curl` to check the app:

```bash
curl http://localhost:5000/
```

4. Get JSON data:

```bash
curl http://localhost:5000/data
```

5. Add new data:

```bash
curl -X POST http://localhost:5000/data      -H "Content-Type: application/json"      -d '{"id": 3, "name": "Charlie"}'
```

6. Check updated data:

```bash
curl http://localhost:5000/data
```

## Stopping Containers

```bash
docker-compose down
```

## Notes

- The app uses `sample_data.json` to store data persistently.
- Changes to `app/` are automatically reflected in the container thanks to volume mounting.
- Health checks ensure the container is running correctly.
