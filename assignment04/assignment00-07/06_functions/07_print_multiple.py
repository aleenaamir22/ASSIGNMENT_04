#print a message multiple times
#Fill out print_multiple(message, repeats), which takes as parameters a string message to print, and an integer repeats number of times to print message. We've written the main() function for you, which prompts the user for a message and a number of repeats.

def print_multiple(message,repeat):#function
      for i in range(repeat):#loop
            print(message)#message printed acc repeat times

def main():
        #user input
        message=str(input('Enter your message: '))
        repeat=int(input('Enter an number(int) of times to repeat the message: '))
        
        times=print_multiple(message,repeat)
        print(f"{message} printed {repeat} times")
if __name__ == '__main__':
    main()        