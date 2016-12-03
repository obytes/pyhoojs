#
# Pull base image.

FROM phusion/passenger-full

# copy our app to /src
COPY . /src

WORKDIR /src
# install app and requirements
RUN apt-get update && apt-get install -y \
    python-dev \
    python-pip

RUN pip install -r requirements/test.txt

RUN npm install

#EXPOSE $PORT

ENTRYPOINT ["/src/entrypoint.sh"]
