#printing the ones digit of a number

def print_ones_digit(num):#required func
    print(f"The ones digit of {num} is:" , num % 10 )#getting remainder
def main():
    number=int(input('Enter a number: '))#user input
    print_ones_digit(number)#calling function
if __name__ == '__main__':
    main()