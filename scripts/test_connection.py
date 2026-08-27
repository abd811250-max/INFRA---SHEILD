import os
import psycopg2


DB_HOST = "127.0.0.1"
DB_PORT = 5432
DB_NAME = "infra_sheild_db"
DB_USER = "postgres"
DB_PASSWORD = os.getenv("DB_PASSWORD")


print("========== DATABASE SETTINGS ==========")
print("Host:", repr(DB_HOST))
print("Port:", repr(DB_PORT))
print("Database:", repr(DB_NAME))
print("User:", repr(DB_USER))
print("=======================================")


try:

    connection = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

    print("\nPostgreSQL connection successful! ✅")

    cursor = connection.cursor()

    cursor.execute("SELECT version();")

    version = cursor.fetchone()

    print("\nPostgreSQL version:")
    print(version[0])

    cursor.close()
    connection.close()

    print("\nConnection closed successfully.")

except Exception as e:

    print("\nConnection failed! ❌")
    print(type(e).__name__)
    print(e)
