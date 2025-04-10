def main():

    fruits_name_price={'apple':50,'durian':60,'kiwi':30,'mango':40,'rambutan':50,'jackfruit':30}#dictionary of fruits and their price
    total=0
    print("\033[1m\033[3m🍉Welcome to Aleena Fruit Shop\033[0m")
    for fruits in fruits_name_price:
        price=fruits_name_price[fruits]#loop
        
        try:
            buy = int(input(f'How many {fruits}s do you want?: '))#user input
        except ValueError:
            buy = 0  
        
        total += price * buy #total amount calculation
    print(f'Your total amount is ${total}')  #response:total money  
if __name__ == '__main__':
    main()    