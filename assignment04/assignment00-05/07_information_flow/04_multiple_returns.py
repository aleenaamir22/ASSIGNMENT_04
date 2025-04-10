#getting user data data and printing multiple data one time

def get_user_data():
    first_name=str(input('Enter your First name: '))#userinput
    last_name=str(input('Enter your Last name: '))#user input
    email=str(input('Enter your Email: '))#user input

    return first_name,last_name,email #returning all the user info

def main():
    user_info=get_user_data()#calling func
    print(f'Received the follwing user info:{user_info}')#response
if __name__ == '__main__':
    main()    