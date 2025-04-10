def main():
    user_input=input("What's your good name: ")#user input
    print(greeting(user_input))#calling function and printing

def greeting(name):
    return "Hi "+ name +" Have a nice day" #return greeting msg
if __name__ == '__main__':
    main()