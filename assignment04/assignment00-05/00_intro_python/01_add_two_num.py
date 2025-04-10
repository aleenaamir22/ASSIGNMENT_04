#Problem statement 01
#Write a Python program that takes two integer inputs from the user and calculates their sum.
#Adding two number
def main():
       num1=int(input('Enter your First Number: ')) #Prompt the user to enter the first number and convert it into integer
       num2=int(input('Enter your Second Number: ')) #Prompt the user to enter the first number and convert it into integer

       total=num1 + num2 #Calculate the sum of the two numbers
       print(f'By adding {num1} and {num2} your answer will be {total}') #Print the total sum with an appropriate message.

if __name__ == '__main__':
    main()