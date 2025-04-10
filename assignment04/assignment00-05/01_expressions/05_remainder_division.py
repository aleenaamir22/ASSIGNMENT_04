#Remainder division
#Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

def main():
     num1=int(input('Enter the integer to be divided: '))#first number
     num2=int(input('Enter the integer to divided by: '))#second number

     quot=int(num1 // num2)#For Quotient
     rem=int(num1 % num2)#For Remainder

     print(f'By dividing {num1} & {num2} , quotient will be {quot} & remainder will be {rem}')#response
     
if __name__ == '__main__':
  main()