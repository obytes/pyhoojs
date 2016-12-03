#
# Pull base image.

FROM phusion/passenger-full


# copy our app to /src
COPY . /src

WORKDIR /src
# install app and requirements

RUN npm install; pip install -r requirements/test.txt

#EXPOSE $PORT

ENTRYPOINT ["/src/entrypoint.sh"]
