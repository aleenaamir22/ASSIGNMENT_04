#number is whether even or odd
#10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd

def is_odd(value: int):
    
    remainder = value % 2  #checking the num is odd
    return remainder == 1 #returning 

def main():
    for i in range(10,20):#loop
        if is_odd(i):#function called
            print(i,'odd' , end=" ")#if num is odd than it will print odd
        else:
            print(i,'even' , end=" ")#if num is even than it will print even

if __name__ == '__main__':
    main()