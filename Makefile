# Define variables
IMAGE_NAME = shopping-list-app
DOCKER_ID_USER = wenyeli
PORT = 5000

# Python commands
install:
	pip install --upgrade pip && pip install -r requirements.txt

run-local:
	python app.py

# Docker commands
image_show:
	docker images

container_show:
	docker ps

login:
	docker login -u $(DOCKER_ID_USER)

build: login
	docker build -t $(IMAGE_NAME) .
	docker tag $(IMAGE_NAME) $(DOCKER_ID_USER)/$(IMAGE_NAME):latest
	docker push $(DOCKER_ID_USER)/$(IMAGE_NAME):latest

run:
	@echo "==> Stopping any containers using port $(PORT)..."
	-docker stop $$(docker ps -q --filter publish=$(PORT))
	@echo "==> Starting new container..."
	docker run -d -p $(PORT):$(PORT) $(IMAGE_NAME)

stop:
	docker stop $$(docker ps -a -q)

clean:
	@echo "==> Stopping containers..."
	-docker stop $$(docker ps -a -q --filter ancestor=$(IMAGE_NAME))
	@echo "==> Removing containers..."
	-docker rm -f $$(docker ps -a -q --filter ancestor=$(IMAGE_NAME))
	@echo "==> Removing image..."
	-docker rmi -f $(IMAGE_NAME)
	@echo "==> Clean complete"

check-port:
	@echo "==> Checking port $(PORT) usage..."
	-docker ps --filter publish=$(PORT)

# Development workflow
dev: build run

.PHONY: install run-local image_show container_show login build run stop clean check-port dev