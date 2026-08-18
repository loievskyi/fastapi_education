BACKEND_CONTAINER = backend1

PHONY: up down build bash

up:
	docker compose up -d

down:
	docker compose down

build:
	docker compose build

bash:
	docker compose exec -it ${BACKEND_CONTAINER} bash
