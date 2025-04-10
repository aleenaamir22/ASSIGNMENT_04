#Problem statement 06
#Ask the user for a number and print its square (the product of the number times itself)

def main():

    num=float(input('\033[1m\033[3m Enter your number:\033[0m ')) #user input is in bold italics
    square=(num * num) #square (multiplying num with num ) #4*4=16
    print(f'\033[1m\033[3m The square of {num} is {square}\033[0m')#output + in bold & italic way

if __name__ == '__main__':
    main()   