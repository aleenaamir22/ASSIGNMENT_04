#We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low 
import random
def main():
    score=0#initial score
    rounds=5#total rounds in game
    for round_num in range(1,rounds+1):#loop
       print(f'\033[1mRound Number:{round_num}\033[0m')
       user_input_number=int(input('Enter a number(1-100): '))#user_input num
       user_input_high_low=str(input('Enter whether your num is high or lower:'))#input higher or lower
       computer_number=random.randint(0,100)#system generating random number
    
    #responses
       print(f"computer number was:{computer_number}")
       if user_input_high_low=='higher'  and user_input_number > computer_number:
          print("You're right!")
          score += 1
       elif user_input_high_low =='lower' and user_input_number < computer_number:
          print("You're right!") 
          score +=1   
       else:
          print("You're wrong!")
    print(f"Game over!Your total score is:{score}")  #total score printed
            
if __name__ == '__main__':
    main()           