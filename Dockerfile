FROM python:3.10.0
RUN pip install --upgrade pip
ADD . /app
WORKDIR /app
RUN pip install -e .