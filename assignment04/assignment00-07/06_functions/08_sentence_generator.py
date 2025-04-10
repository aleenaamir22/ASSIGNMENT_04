#generating sentences with help of user input

def make_sentence(word:str, part_of_speech:int): 
    
    if part_of_speech==0:
        print(f"I saw a {word} at the park today")#for noun
    elif part_of_speech==1:
        print(f"The sky looked so {word} this evening.")#for adjective    
    elif part_of_speech==2:
        print(f"Every morning, I like to {word} before breakfast.")#for verb    
    else:
        print("Please enter the valid numbers 0, 1, or 2.")  #error

def main():
    user_input_word=str(input("Enter a noun,adjective,verb of your choice: "))
    user_input_speech=int(input('Enter 0 for noun,1 for adjective,2 for verb: '))
    make_sentence(user_input_word,user_input_speech)#calling function
if __name__ == '__main__':
    main()  