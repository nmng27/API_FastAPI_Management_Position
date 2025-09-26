import psycopg2

def get_connection():
    conn = psycopg2.connect(
        dbname="PositionManagement",
        user="postgres",
        password="nmng27",
        host="localhost",
        port="5431"
    )
    return conn
