import random

def main():
     random_no=10 #total no of eandom numbers to generate
     
     for i in range(random_no):#loop
          num = random.randint(1, 100)#random number will come from this (1-100)
          print(num , end= ' ') #response : any 10 random numbers from1 to 100 will print

if __name__ == '__main__':
    main()