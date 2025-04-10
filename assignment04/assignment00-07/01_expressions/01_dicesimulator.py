#Dicesimulator 01
#Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.
import random
def main():

     print("Rolled the dice three times:") #msg before rolling dies
for _ in range(3):#loop
    
     dies1=random.randint(1,6) #dies1 random number from 1 to 6
     dies2=random.randint(1,6) #dies2 random number from 1 to 6
     
     print(f"Die 1: {dies1}, Die 2: {dies2}")#printing random 1 to 6 number for each dies

     

if __name__ == '__main__' :   
     main()