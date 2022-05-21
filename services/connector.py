import psycopg2

conn = psycopg2.connect(database="Online_Shop",
                        user='postgres',
                        password='0147',
                        host='localhost',
                        port='5432')
cursor = conn.cursor()
conn.autocommit = True

# data = cursor.fetchone()
# conn.close()
