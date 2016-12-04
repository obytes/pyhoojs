#
# Pull base image.

FROM chenglongzq/pyhoojs

###################### copy our app to /src
COPY . /src

WORKDIR /src

RUN pip install -r requirements/test.txt

RUN npm install

#EXPOSE $PORT

ENTRYPOINT ["/src/entrypoint.sh"]
