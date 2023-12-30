import psycopg2
import os


conn = psycopg2.connect(
    dbname=os.environ.get('POSTGRES_DB'),
    user=os.environ.get('POSTGRES_USER'),
    password=os.environ.get('POSTGRES_PASSWORD'),
    host=os.environ.get('POSTGRES_HOST'),
    port=os.environ.get('POSTGRES_PORT')
    )

cursor = conn.cursor()

## Open a cursor to perform database operations
cur = conn.cursor()

## drop any existing todos table
cur.execute("DROP TABLE IF EXISTS todos;")

## (re)create the todos table
## (note: triple quotes allow multiline text in python)
cur.execute("""
  CREATE TABLE todos (
    id serial PRIMARY KEY,
    description VARCHAR NOT NULL
  );
""")

## commit, so it does the executions on the db and persists in the db
conn.commit()

cur.close()
conn.close()
