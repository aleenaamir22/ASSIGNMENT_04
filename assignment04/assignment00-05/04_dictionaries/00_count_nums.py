#This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

def main():
    numbers = {}  # Dictionary to store all the numbers

    while True:
        number = input("Enter a number: ")

        if number == "":
            break  #breal from user input
        if number in numbers:
            numbers[number] += 1
        else:
            numbers[number] = 1

    
    for number, count in numbers.items():
        print(f"{number} appears {count} times.")# Printing all number and how many times it appeares
        
if __name__ == '__main__':
    main()
