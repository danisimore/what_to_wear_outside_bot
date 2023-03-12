import psycopg2


def insert_data(host, user, password, db_name, identifier, name, latitude, longitude):

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
            print('[INFO] Data inserted successfully')

        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection closed')

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)

