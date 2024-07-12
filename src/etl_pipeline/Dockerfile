FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY etl_task_definitions /app/etl_task_definitions
COPY ETLPipeline /app/ETLPipeline
COPY main.py /app/main.py

CMD [ "python3", "main.py" ]