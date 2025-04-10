#printing random num until it wants from 1-10
#chaotic count

import random

DONE_LIKELIHOOD = 0.1  #chance to stop

def done():
    return random.random() < DONE_LIKELIHOOD #random number

def chaotic_counting():
    for i in range(1, 11):#loop
        if done():
            return  #stop the count and print
        print(i)

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")#print
    chaotic_counting()#loop till done with count
    print("I'm done.")#response

if __name__ == '__main__':
    main()
