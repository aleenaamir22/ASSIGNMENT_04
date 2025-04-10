#get your name with msg
#Fill out the get_name() function to return your name as a string! We've written a main() function for you which calls your function to retrieve your name and then prints it in a greeting.

def get_name():
    return "Aleena"

def main():
    your_name=get_name()#calling func
    print(f'Hi {your_name},have a nice day!!')
if __name__ == '__main__':
    main()    

#user input 
def get_name(name):
    return (name)

def main():
    user_input=input('Enter your name: ')
    your_name=get_name(user_input)#calling func
    print(f'Hi {your_name},have a nice day!!')
if __name__ == '__main__':
    main()    