FROM python:3.7-alpine3.9

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

WORKDIR /app
COPY . /app

ENTRYPOINT ["python3.7", "run.py"]
