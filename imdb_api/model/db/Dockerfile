FROM postgres

COPY create_db.sql /docker-entrypoint-initdb.d/
COPY insert_data.sql .

EXPOSE 5432
