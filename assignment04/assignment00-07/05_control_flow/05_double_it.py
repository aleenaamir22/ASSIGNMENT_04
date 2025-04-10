#05_double_it
#Write a program that asks a user to enter a number. Your program will then double that number and print out the result.

def main():
    print("🔁 Double Your Number Until It Reaches 100 or More")

    user_input = int(input("Enter a number (integer): "))

    while user_input < 100:
        user_input = user_input * 2
        print(user_input, end=" ")
    else:
        print("Invalid request")    

if __name__ == '__main__':
    main()
