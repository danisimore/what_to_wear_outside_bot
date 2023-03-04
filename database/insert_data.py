import os
import psycopg2
from dotenv import load_dotenv

load_dotenv('.env.db.config')


def test_name_for_func(host, user, password, db_name, identifier, name, latitude, longitude):

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
                f'''INSERT INTO users VALUES
                ({identifier}, {str(name)}, {latitude}, {longitude})
                ;'''
            )
            print('[INFO] Table created successfully')

        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection closed')

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)

