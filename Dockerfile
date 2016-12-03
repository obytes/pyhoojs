
FROM debian:latest

MAINTAINER Mr. Chenglong <chenglong.zq@gmail.com>

RUN apt-get update

# copy our app to /src
COPY . /src

WORKDIR /src
# install app and requirements

RUN cd /src; npm install; pip install -r requirements/test.txt


ENTRYPOINT ["docker-entrypoint.sh"]
