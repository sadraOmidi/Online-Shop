from services import connector


def insert_new_user(name, city, province, email, password, mobile):
    connector.cursor.execute(
        'INSERT INTO public."user"(name, city, province, email, password, mobile) VALUES (%s, %s, %s, %s, %s, %s)',
        (name, city, province, email, password, mobile))
    connector.conn.close()


def update_user(name, mobile, city, province, email, password, id):
    connector.cursor.execute(
        '''UPDATE public."user" SET "name" = %s, "city" = %s, "province" = %s, "email" = %s, "password" = %s,
         "mobile" = %s WHERE "ID" = %s''',
        (name, city, province, email, password, mobile, id))
    connector.conn.close()


def delete_user(id):
    connector.cursor.execute('''DELETE FROM public."user" WHERE "ID" = %s''', (id,))
    connector.conn.close()


def select_user(EMAIL):
    connector.cursor.execute(
        '''SELECT * FROM public."user" WHERE "email" = %s ''', (EMAIL,))
    result = connector.cursor.fetchmany()
    id, email, password, city, province = result[0][0], result[0][4], result[0][5], result[0][
        2], result[0][3]
    return {
        'ID': id,
        'EMAIL': email,
        'PASSWORD': password,
        'CITY': city,
        'PROVINCE': province
    }
