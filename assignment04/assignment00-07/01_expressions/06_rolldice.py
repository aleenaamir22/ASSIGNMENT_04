#rolldice
#Simulate rolling two dice, and prints results of each roll as well as the total.
import random
def main():
     dice1=random.randint(1,6)#random number (1 to 6)
     dice2=random.randint(1,6)#random integer (1 to 6)

     total=int(dice1 + dice2)#sum of the random numbers

     print(f'Dice1: {dice1} & Dice2: {dice2}')#printing the random number which comes out while simulating two dies
     print(f'By adding {dice1} & {dice2} the total will be {total}')#printing result of adding two random number which comes out after simulating  two dice

if __name__ == '__main__':
        main()