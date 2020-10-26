FROM python:3.8.2

WORKDIR /imdb_email_service

COPY . .

RUN pip install -r docker/dependencies

CMD python service.py