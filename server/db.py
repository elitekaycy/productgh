import psycopg2

# Replace these with your actual database credentials
DB_HOST = 'localhost'
DB_NAME = 'productgh'
DB_USER = 'postgres'
DB_PASSWORD = 'root'
DB_PORT = 5432


def create_connection():
    connection = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD

    )
    print("connection created")
    return connection


def create_table_if_not_exists():
    connection = create_connection()
    cursor = connection.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS product_metadata (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        clicks INTEGER,
        number INTEGER
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully!")

    cursor.close()
    connection.close()
