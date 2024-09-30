FROM python:3.10-slim

RUN mkdir -m 777 /app

RUN pip install poetry==1.8

COPY . .

WORKDIR /app/

RUN poetry --no-root install

ENTRYPOINT [ "poetry", "run", "python", "main.py" ]