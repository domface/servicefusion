
FROM python:3.5
MAINTAINER Dominik Andrzejczuk <dom@jawn.it>
EXPOSE 80 8000
RUN adduser --disabled-password --gecos '' myuser
RUN apt-get update
RUN apt-get install -y python-pip python-dev libpq-dev postgresql postgresql-contrib


WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
COPY start.sh /app/start.sh


CMD ["/app/start.sh"]
