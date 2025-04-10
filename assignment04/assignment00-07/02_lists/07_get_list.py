#get list

def main():
    user_list = [] #empty list where elements will combine 
    while True:#loop
        item = input(f"Enter element or press enter to exit: ") #input will be extend as wanted by the user
        if item == "": #empty input to brak and creating a list
         break #exiting the loop
        user_list.append(item)  #add user input to the list

    print(f"List: {user_list}")
if __name__ == '__main__':
    main()        