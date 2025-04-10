#count even
#print only even number from the list list will be creating with the help of user input

def even_count(numbers): #func counts even num in list
      count=0
      for num in numbers:
        if num % 2 == 0: #checking if the number even num
           count += 1 #increase count if it is even
      return count # return total count of even num
def main():
     numbers=[]#empty list
     while True:#loop
        user_input=input('Enter a integer number (or just press enter to stop): ')
        if user_input=="":# if user input is empty 
            break #when user input is empty it will be break from here and print the result
        numbers.append(int(user_input))#adding user input in empty list
        even = even_count(numbers)#calling event count func
     print(numbers , end=" ")#printing list
      
     print(f"\nThere are {even} even number in the list")#printing the count of even numbers from the list
if __name__ == '__main__':
    main()

