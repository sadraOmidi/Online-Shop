from user import user
from admin import admin
from product import product
from services import user_crud
from services import admin_crud
from services import product_crud
from time import sleep
import os
from tabulate import tabulate

os.system('cls')
print('\t\t\t***welcome to online shop***\n1.sign up\n2.log in')
answer = input('Enter the desired number -> : ')

# sign up user/admin
if answer == '1':
    sleep(0.3)
    os.system('cls')
    sign_up_answer = input(
        '1.sign up new user\n2.sign up new admin\nEnter the desired number -> : '
    )

    # sign up new user
    if sign_up_answer == '1':
        sleep(0.2)
        os.system('cls')
        name = input('USER -> Enter your name : ')
        mobile = input('USER -> Enter your mobile number : ')
        city = input('USER -> Enter your city : ')
        province = input('USER -> Enter your province : ')
        email = input('USER -> Enter your email : ')
        password = input('USER -> Enter your password : ')
        new_user = user.SignUp(name, mobile, city, province, email, password)
        user_crud.insert_new_user(new_user.name, new_user.city,
                                  new_user.province, new_user.email,
                                  new_user.password, new_user.mobile)
        sleep(0.2)
        os.system('cls')
        print(
            f"*** USER: {new_user.name} ***, you have been successfully registered in the system"
        )
        sleep(5)
        os.system('cls')

    # sign up new admin
    if sign_up_answer == '2':
        sleep(0.2)
        os.system('cls')
        email = input('ADMIN -> Enter your email : ')
        password = input('ADMIN -> Enter your password : ')
        city = input('ADMIN -> Enter your city : ')
        province = input('ADMIN -> Enter your province : ')
        new_admin = admin.SignUp(email, password, city, province)
        admin_crud.insert_new_admin(new_admin.email, new_admin.password,
                                    new_admin.city, new_admin.province)
        sleep(0.2)
        os.system('cls')
        print(
            f"*** ADMIN: {new_admin.email} ***, you have been successfully registered in the system"
        )
        sleep(5)
        os.system('cls')

# log in user/admin
elif answer == '2':
    sleep(0.3)
    os.system('cls')
    log_in_answer = input(
        '1.login user\n2.login admin\nEnter the desired number -> : ')

    # log in user
    if log_in_answer == '1':
        sleep(0.2)
        os.system('cls')
        email_login = input('USER -> Enter your email address: ')
        password_login = input('USER -> Enter your password: ')
        sleep(0.2)
        os.system('cls')
        password_in_db = user_crud.select_user(email_login)['PASSWORD']
        log_in_user = user.LogIn(email_login, password_login)
        if password_in_db == log_in_user.password:
            print(f'*** {email_login} is LOGGED IN ! (user) ***')
            sleep(3)
            os.system('cls')

            options = input(
                '''1.Edit your information\n2.Delete your account\n3.View the my shopping cart\n
                Enter the desired number -> : '''
            )
            # edit information(user)
            if options == '1':
                sleep(0.2)
                os.system('cls')
                name = input('Enter your name : ')
                mobile = input('Enter your mobile number : ')
                city = input('Enter your city : ')
                province = input('Enter your province : ')
                email = input('Enter your email : ')
                password = input('Enter your password : ')
                sleep(0.2)
                os.system('cls')
                editor = user.EditProfile(name, mobile, city, province, email,
                                          password)
                user_crud.update_user(
                    name=editor.name,
                    city=editor.city,
                    province=province,
                    email=editor.email,
                    password=editor.password,
                    mobile=editor.mobile,
                    id=user_crud.select_user(email_login)["ID"])
                print(f"{email} your information was updated!")
                sleep(1.3)
                os.system('cls')

            # delete account (user)
            if options == '2':
                os.system('cls')
                last_question = input('Do you really want to delete your account?\n1.Yes\n2.No\n')
                if last_question == '1':
                    user_id = user_crud.select_user(email_login)['ID']
                    user_crud.delete_user(user_id)
                    print(f"{email_login} DELETED !!!")
                    sleep(2.5)
                    os.system('cls')
                else:
                    print('Account could not be deleted')
                    sleep(2.5)
                    os.system('cls')

            # view shopping cart
            if options == '3':
                os.system('cls')
                print("products list : ")
                product_data = []
                for i in product_crud.select_product():
                    product_data.append(list(i)[1:5])
                col_names = ['code', 'name', 'price($)', 'count']
                print(tabulate(product_data, headers=col_names, tablefmt="fancy_grid"))
                shopping_cart = []
                print("Add the desired 'code' to add to cart :\nEnter 0 to exit and display the shopping cart ")
                while True:
                    user_input = input()
                    shopping_cart.append(user_input)
                    if user_input == '0':
                        break
                os.system('cls')
                user_product_data = []
                sum_of_product_price = 0
                for i in shopping_cart:
                    for j in product_crud.return_product(i):
                        sum_of_product_price += j[2]
                        user_product_data.append(j)
                col_names = ['code', 'name', 'price($)']
                print(tabulate(user_product_data, headers=col_names, tablefmt="fancy_grid"))
                print(f"Amount you can pay: $ {sum_of_product_price}")
                user_answer = input('Do you want to pay?\n1.pay\n2.exit\nEnter the desired number -> : ')
                os.system('cls')
                if user_answer == '1':
                    print("**** Payment was successful. ****")
                    sleep(2)
                    os.system('cls')
                if user_answer == '2':
                    print("*** Payment canceled ***")
                    sleep(2)
                    os.system('cls')

    # log in admin
    if log_in_answer == '2':
        sleep(0.2)
        os.system('cls')
        email_login_admin = input('ADMIN -> Enter your email address: ')
        password_login_admin = input('ADMIN -> Enter your password: ')
        sleep(0.2)
        os.system('cls')
        password_in_db = admin_crud.select_admin(email_login_admin)['PASSWORD']
        log_in_admin = admin.LogIn(email_login_admin, password_login_admin)
        if password_in_db == log_in_admin.password:
            print(f'*** {email_login_admin} is LOGGED IN ! (ADMIN) ***')
            sleep(3)
            os.system('cls')

            options_admin = input(
                '''1.Edit your information\n2.Delete your account\n3.Insert a new product\n4.Delete a product
5.View all product\nEnter the desired number -> : '''
            )

            # edit information
            if options_admin == '1':
                sleep(0.2)
                os.system('cls')
                email = input('Enter your email : ')
                password = input('Enter your password : ')
                city = input('Enter your city : ')
                province = input('Enter your province : ')
                sleep(0.2)
                os.system('cls')
                editor = admin.EditProfile(email, password, city, province)
                admin_crud.update_admin(
                    email=editor.email,
                    password=editor.password,
                    city=editor.city,
                    province=province,
                    id=admin_crud.select_admin(email_login_admin)["ID"])
                print(f"{email} your information was updated!")
                sleep(2)
                os.system('cls')

            # delete account
            if options_admin == '2':
                os.system('cls')
                last_question = input('Do you really want to delete your account?\n1.Yes\n2.No\n')
                if last_question == '1':
                    admin_id = admin_crud.select_admin(email_login_admin)['ID']
                    admin_crud.delete_admin(admin_id)
                    os.system('cls')
                    print(f"{email_login_admin} DELETED !!!")
                    sleep(2.5)
                    os.system('cls')
                else:
                    print('Account could not be deleted')
                    sleep(2.5)
                    os.system('cls')

            # insert product
            if options_admin == '3':
                os.system('cls')
                product_name = input("Please enter a product name: ")
                product_price = input("Please enter a product price: ")
                product_count = input("Please enter the number in stock: ")
                p = product.Product(product_name, product_price, product_count)
                product_crud.insert_product(
                    p.name, p.price, p.count, p.product_code, admin_crud.select_admin(email_login_admin)["ID"]
                )
                os.system('cls')
                print(f'New product added successfully')
                sleep(3)
                os.system('cls')

            # delete product
            if options_admin == '4':
                os.system('cls')
                product_data = []
                for i in product_crud.select_product():
                    product_data.append(list(i)[1:4])

                col_names = ['code', 'name', 'price($)', 'count']
                print(tabulate(product_data, headers=col_names, tablefmt="fancy_grid"))
                product_code = input("\nEnter the product code to delete: ")
                last_question = input('Do you really want to delete this product?\n1.Yes\n2.No\n')
                if last_question == '1':
                    product_crud.delete_product(product_code)
                    print("DELETED !!!")
                    sleep(2.5)
                    os.system('cls')
                else:
                    print("product code is wrong !")
                    sleep(2.5)
                    os.system('cls')

            # see all product
            if options_admin == '5':
                os.system('cls')
                product_data = []
                for i in product_crud.select_product():
                    product_data.append(list(i))

                col_names = ['ID', 'code', 'name', 'price($)', 'count', 'created by (admin)']
                print(tabulate(product_data, headers=col_names, tablefmt="fancy_grid"))
