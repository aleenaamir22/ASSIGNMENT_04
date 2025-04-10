#Write a program that prints out the calls for a spaceship that is about to launch. Countdown from 10 to 1 and then output Liftoff!
import time
def main():
    for i in range(10,0,-1):#countdown from 10 to 1 #loop
        print(i)#countdown
        time.sleep(1)#wait for 1 sec and print countdown
    print("Liftoff!")#response printed
if __name__ == '__main__':
    main() 