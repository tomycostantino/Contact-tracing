FROM python:latest

RUN apt-get update && apt-get install -y libgmp-dev

WORKDIR .

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "tracker_docker.py"]