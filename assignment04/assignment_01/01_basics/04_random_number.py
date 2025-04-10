#Print 10 random numbers in the range 1 to 100.

import random

def main():
    for i in range(10):#loop
        print(random.randint(1,100), end=" ")#printing 10 random numbers
if __name__ == '__main__':
    main()        