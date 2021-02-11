FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /message_project
COPY requirements.txt /message_project/
RUN pip install -r requirements.txt
COPY . /message_project/