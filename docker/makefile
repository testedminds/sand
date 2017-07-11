SHELL = /usr/bin/env bash

img = testedminds/$(img-name)
latest = $(img):latest

docker-all: docker-stop docker-build docker-run docker-open

docker-build:
	docker build -t $(latest) -f docker/Dockerfile .

docker-stop:
	-docker stop $(img-name)

docker-push:
	docker tag $(latest) $(img):$(version)
	docker push $(latest)
	docker push $(img):$(version)

docker-machine:
	docker-machine create --driver virtualbox --virtualbox-memory '4096' default

docker-run:
	docker run -d -p 80:8888 -v `pwd`/docs:/opt/sand --rm --name $(img-name) $(latest) \
		jupyter notebook --allow-root --ip 0.0.0.0 --no-browser --NotebookApp.token=''

docker-docs: docker-stop docker-run

docker-open:
	open http://192.168.99.100
