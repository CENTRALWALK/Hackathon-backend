FROM python:3.8-slim-buster

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT ["flask"]

CMD ["run", "--host", "0.0.0.0"]

