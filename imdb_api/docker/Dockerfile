FROM python:3.8.2

WORKDIR /imdb_api

COPY . .

RUN pip install -r docker/dependencies

ENV FLASK_APP imdb_api
ENV FLASK_ENV development

EXPOSE 8899

CMD python serve.py