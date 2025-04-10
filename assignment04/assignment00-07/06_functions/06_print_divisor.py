#printing divisor of a num
#Write the helper function print_divisors(num), which takes in a number and prints all of its divisors (all the numbers from 1 to num inclusive that num can be cleanly divided by (there is no remainder to the division). Don't forget to call your function in main()!


def print_divisor(num:int):
    for i in range(num):#loop
        div=i + 1# We add 1 because range starts from 0, but divisors start from 1
        if num % div == 0: # Check if 'div' is a divisor of 'num'
          print(div)   #If it divides evenly, print the divisor

def main():
   user_input=int(input('Enter a number: ')) # Prompt the user to enter a numbe
   print_divisor(user_input)#calling func

if __name__ == '__main__':
    main()            