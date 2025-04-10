#double your number
#Fill out the double(num) function to return the result of multiplying num by 2. We've written a main() function for you which asks the user for a number, calls your code for double(num) , and prints the result.

def double_num(num):
    return(num * 2) #double the num by multiplying the num

def main():
     user_input=int(input('Enter a integer number: '))#user promt
     doubled=double_num(user_input)#calling double_num func
     print(f'Double of {user_input} if {doubled}')#output
if __name__ == '__main__':
     main()     