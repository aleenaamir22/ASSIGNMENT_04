def adult_age(age):
    maximum_age=18 #max age
    if age >= maximum_age:#condition
        return True
    else:
        return False

def main():
    user_input=int(input('Enter your age(integer):'))#user input
    Adult_age=adult_age(user_input)#calling func
    if Adult_age:
     print(f"True:You're {user_input} year old, you can ride the motorbike")#output if cond is true
    else:
       print(f"False:You're {user_input} year old, you cannot ride the motorbike")#output if cond is false

if __name__ == '__main__':
   main()        
