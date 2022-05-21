# from sys import argv
from services import connector


def insert_new_admin(email, password, city, province):
    connector.cursor.execute(
        '''INSERT INTO public."admin" (email, password, city, province) VALUES (%s, %s, %s, %s)''',
        (email, password, city, province))
    connector.conn.close()


def update_admin(email, password, city, province, id):
    connector.cursor.execute('''UPDATE public."admin" SET "email" = %s, "password" = %s, "city" = %s, "province" = %s
    WHERE "ID" = %s''', (email, password, city, province, id))
    connector.conn.close()


def delete_admin(id):
    connector.cursor.execute('''DELETE FROM public."admin" WHERE "ID" = %s''', (id,))
    connector.conn.close()


def select_admin(EMAIL):
    connector.cursor.execute(
        '''SELECT * FROM public."admin" WHERE "email" = %s ''', (EMAIL,))
    result = connector.cursor.fetchmany()
    id, email, password, city, province = result[0][0], result[0][1], result[0][2], result[0][
        3], result[0][4]
    return {
        'ID': id,
        'EMAIL': email,
        'PASSWORD': password,
        'CITY': city,
        'PROVINCE': province
    }
