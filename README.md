[![CI](https://github.com/nogibjj/Wenye_Li_Individual_Project_3/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Wenye_Li_Individual_Project_3/actions/workflows/cicd.yml)

## Wenye Li Individual Project 3

### Video

### Project Overview

This project implements an auto-scaling Flask application that integrates with TinyLlama through Ollama for natural language processing capabilities. The application provides a real-time chat interface and is deployed using AWS App Runner for automatic scaling.

### Local Development

```bash
# Install dependencies
make install

# Install and start Ollama
curl https://ollama.ai/install.sh | sh
ollama serve
ollama pull tinyllama

# Run application
make run-local
```

### Docker Deployment

```bash
# Build and run
make build
make run
```

### Use of DockerHub (Or equivalent)

Functioning container is held on DockerHub and ECR.

```bash
docker pull wenyeli/chatbot
```

![ECR](ECR.png)

### AWS App Runner Deployment

https://g2wttvnjwp.us-east-1.awsapprunner.com/

Deploy using AWS App Runner.
![runner](runner.png)
