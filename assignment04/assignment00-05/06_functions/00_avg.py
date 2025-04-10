#taking average
#Write a function that takes two numbers and finds the average between the two.

def average(a,b): #avg func
     sum=a+b
     return(sum/2)


def main():
     a=float(input('Enter a your first number: '))#first input
     b=float(input('Enter a your second number: '))#sec input
     avg = average(a,b) #calling function
     print(f'The average of {a} and {b} is {avg}') #response:printing avg of two terms getting from user input

if __name__ == '__main__':
    main()