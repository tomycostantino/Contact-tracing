FROM python:latest

#RUN apt-get update && apt-get install -y libgmp-dev

WORKDIR .

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Create a volume for storing the database
VOLUME /database

# Set the working directory and command to run your program
WORKDIR .

CMD ["python", "run_tracker.py"]