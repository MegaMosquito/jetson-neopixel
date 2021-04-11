# Container that displays pretty patterns on NeoPixel strings on Jetsons.

DOCKERHUB_ID:=ibmosquito
NAME:="jetson-neopixel"
VERSION:="1.0.0"

defaut: build run

build:
	docker build -t $(DOCKERHUB_ID)/$(NAME):$(VERSION) .

dev: stop
	docker run -it -v `pwd`:/outside \
	  --privileged \
	  --name ${NAME} \
	  $(DOCKERHUB_ID)/$(NAME):$(VERSION) /bin/bash

run: stop
	docker run -d \
	  --privileged \
	  --restart unless-stopped \
	  --name ${NAME} \
	  $(DOCKERHUB_ID)/$(NAME):$(VERSION)

push:
	docker push $(DOCKERHUB_ID)/$(NAME):$(VERSION) 

stop:
	@docker rm -f ${NAME} >/dev/null 2>&1 || :

clean:
	@docker rmi -f $(DOCKERHUB_ID)/$(NAME):$(VERSION) >/dev/null 2>&1 || :

.PHONY: build dev run push stop clean

