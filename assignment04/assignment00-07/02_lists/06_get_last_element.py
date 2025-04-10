# get last element

def main():
    num = int(input("How many elements do you want to enter? ")) #number of elements a user want to input
    user_list = [] #elements will combine to make a list

    for i in range(num):
        item = input(f"Enter element {i+1}: ") #input will be extend as wanted by the user
        user_list.append(item) #adding items to list

    print("Full list:", user_list) #first list will be printed
    print("Last element:", user_list[-1]) #last element will be printed

if __name__ == '__main__':
    main()