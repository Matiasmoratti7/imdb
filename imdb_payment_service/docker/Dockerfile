FROM python:3.8.2

WORKDIR /imdb_payment_service

COPY . .

RUN pip install -r docker/dependencies

ENV FLASK_APP imdb_payment_service
ENV FLASK_ENV development

EXPOSE 4000

CMD python serve.py