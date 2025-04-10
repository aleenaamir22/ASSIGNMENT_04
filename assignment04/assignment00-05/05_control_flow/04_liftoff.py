#04_liftoff timer countdown
#Write a program that prints out the calls for a spaceship that is about to launch. Countdown from 10 to 1 and then output Liftoff!

import time

def main():
   
       for i in range(10,0,-1):#countdown
             print(i)#printing countdown
             time.sleep(1)#waiting for 1 sec to print another num.
       print("Liftoff")#response

if __name__ == '__main__':
    main()    