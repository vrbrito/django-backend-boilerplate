.PHONY: up
up:
	docker-compose up

.PHONY: upd
upd:
	docker-compose up -d

.PHONY: down
down:
	docker-compose down

.PHONY: shell-django
shell-django:
	docker-compose exec application sh

.PHONY: logs-django
logs-django:
	docker-compose logs -f application

.PHONY: build
build:
	docker build -t application .

# .PHONY: push
# push:
# 	docker tag application docker_hub_address
# 	docker push docker_hub_address