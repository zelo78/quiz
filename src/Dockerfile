FROM python:3.10.8
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY . /app

RUN pip install --upgrade pip
RUN pip install -Ur  /app/requirements.txt
