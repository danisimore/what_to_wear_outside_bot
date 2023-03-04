import os
import psycopg2
from dotenv import load_dotenv

load_dotenv('.env.db.config')


def create_table():
    host = os.environ.get('HOST')
    user = os.environ.get('DB_USER')
    password = os.environ.get('PASSWORD')
    db_name = os.environ.get('DB_NAME')

    try:
        # connect to exists database
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                '''CREATE TABLE users(
                id bigint PRIMARY KEY,
                name varchar(150) NOT NULL,
                latitude numeric NOT NULL,
                longitude numeric NOT NULL
                );'''
            )
            print('[INFO] Table created successfully')

        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection closed')

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)


create_table()
