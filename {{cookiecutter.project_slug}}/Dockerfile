FROM amd64/python:3.9.0-slim-buster

# define some environment variables
ENV WORKDIR=/usr/src/app
ENV USER=app
ENV APP_HOME=/home/app/web

# set some environment variables inside the Docker container
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

# set the path where the command, defined with CMD, is to be executed inside the Docker container
WORKDIR ${WORKDIR}

RUN pip install --upgrade pip

# copy the requirements.txt file into the WORKDIR location
COPY ./requirements.txt ${WORKDIR}/requirements.txt

# install 'gcc' compiler
RUN apt update && apt install build-essential -y

RUN pip install -r requirements.txt

# create a system user to run the app
RUN adduser --system --group ${USER}

RUN mkdir ${APP_HOME}

# change the working directory
WORKDIR ${APP_HOME}

COPY . ${APP_HOME}

RUN chown -R ${USER}:${USER} ${APP_HOME}

# set the username which is to run the container
USER ${USER}