import psycopg2


class User:

    def __init__(self, host, user, password, db_name, identifier):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name
        self.identifier = identifier

    def check_user(self):
        try:
            # connect to exists database
            connection = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db_name
            )

            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    f'''
                    SELECT * FROM users
                    WHERE id = {self.identifier}
                    ;'''
                )
                user = cursor.fetchall()
                print('[INFO] User check was successful')

            if connection:
                connection.close()
                print('[INFO] PostgreSQL connection closed')

            return user

        except Exception as _ex:
            print('[INFO] Error while working with PostgreSQL', _ex)

    def save_id(self):
        try:
            # connect to exists database
            connection = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db_name
            )

            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    f'''
                    INSERT INTO users (id) VALUES
                    ({self.identifier})
                    ;'''
                )
                print('[INFO] Data inserted successfully')

            if connection:
                connection.close()
                print('[INFO] PostgreSQL connection closed')


        except Exception as _ex:
            print('[INFO] Error while working with PostgreSQL', _ex)

