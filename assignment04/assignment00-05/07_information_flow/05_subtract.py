#Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.

def subtRact_seven(num):
    number=num - 7 #SUBSTRACTING 7 FROM THE INPUT NUM
    return number #RETURNING THE RESULT

def main():
    user_input=int(input('Enter a number: '))#USER INPUT
    subtracting=subtRact_seven(user_input)#CALLING FUNC
    print(subtracting)#PRINTING RESPONSE

if __name__ == '__main__':
    main()    
