.PHONY: build_start down start_local

# Docker build and start the local docker stack
build_start_common:
	docker compose -f docker-compose.yml build --no-cache && docker compose -f docker-compose.yml up --force-recreate  $(c)

build_start_form_handler:
	docker compose -f docker-compose-form-handler.yml build --no-cache && docker compose -f docker-compose-form-handler.yml up --force-recreate  $(c)

start_local:
	docker compose -f docker-compose.yml up -d --force-recreate  $(c)

# Stop the local docker stack
down_common:
	docker compose -f docker-compose.yml down $(c)

down_form_handler:
	docker compose -f docker-compose-form-handler.yml down $(c)