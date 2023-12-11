FROM python:3.11.1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /catschat
COPY requirements.txt /catschat/requirements.txt
RUN pip install django djangorestframework channels_redis django-cors-headers python-dotenv
RUN pip install -U channels["daphne"]
COPY . /catschat