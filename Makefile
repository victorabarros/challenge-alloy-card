APP_NAME?=chess-game-api
API_BASE_IMAGE=python:3.9
CONTAINER_NAME=${APP_NAME}
PWD=$(shell pwd)


debug:
	@make remove-containers CONTAINER_NAME=${APP_NAME}-debug
	@echo "\e[1m\033[33mDebug mode\e[0m"
	@docker run -it -v ${PWD}:${PWD} -w ${PWD} \
		-p 8081:8081 --env-file .env --rm --name ${APP_NAME}-debug \
		${API_BASE_IMAGE} bash

remove-containers:
	@echo "Removing containers"
ifneq ($(shell docker ps -a --filter "name=${CONTAINER_NAME}" -q 2> /dev/null | wc -l | bc), 0)
	@docker ps -a --filter "name=${CONTAINER_NAME}" -q | xargs docker rm -f
endif

remove-images:
	@echo "Removing images"
ifneq ($(shell docker images -a hu/${CONTAINER_NAME}* -q 2> /dev/null | wc -l | bc), 0)
	@docker images -a hu/${CONTAINER_NAME}* -q | xargs docker rmi -f
endif

remove-all: remove-containers remove-images

ips:
	@echo "\e[1m\033[33mips\e[0m"
	@docker ps -q --filter "name=${APP_NAME}" | xargs docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'
