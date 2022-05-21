from services import connector


def insert_product(product_name, product_price, count, product_code, admin_id):
    connector.cursor.execute(
        '''INSERT INTO public."product"(product_name, product_price, count, product_code, admin_id)
         VALUES (%s, %s, %s, %s, %s)''', (product_name, product_price, count, product_code, admin_id)
    )
    connector.conn.close()


def update_product():
    pass


def delete_product(product_code):
    connector.cursor.execute(
        '''DELETE FROM public."product" WHERE "product_code" = %s''', (product_code,)
    )
    connector.conn.close()


def search_product():
    pass


def return_product(product_code):
    connector.cursor.execute(
        '''SELECT product_code, product_name, product_price FROM public."product" WHERE product_code = %s''',
        (product_code,)
    )
    result = connector.cursor.fetchall()
    return result


def select_product():
    connector.cursor.execute('''SELECT * FROM public."product"''')
    result = connector.cursor.fetchall()
    return result
