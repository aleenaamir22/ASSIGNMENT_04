#Print events
#Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort

def main():
    
      num=20 #total even numbers we need

      for i in range(num): #loop
           even_num= i * 2

           print(even_num , end=" ")#response +printing response on same line
           
if __name__ == '__main__':
    main()
