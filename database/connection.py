import psycopg2

class Connect:
    conn = psycopg2.connect(
        database="healthdb",
        user="postgres",
        password="password",
        host="health_status_calculator-database-1",
        port="5432"
    )
