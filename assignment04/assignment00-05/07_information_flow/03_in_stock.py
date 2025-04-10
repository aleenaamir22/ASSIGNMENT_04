#a fruit shop stock 

def in_stock(fruit):#function
     stored= {#template
        'apple': 10,
        'banana': 5,
        'orange': 0,
        'mango': 7,
        'grape': 3,
        'kiwi':5,
        'pineapple':8,
    }
     return stored.get(fruit.lower(),0)#how many stock is available

def main():
    print("🍉Welcome to Sophia Fruit Shop")
    print("We sell fresh fruits like:apple,orange:pineapple,kiwi,mango etc.\nTell us what do you want?")
    fruit_want=str(input('Enter a fruit: ')) #user input
    stock=in_stock(fruit_want)   #calling function
    if stock == 0:
        print(f'Sorry!This fruit is not in stock \n {fruit_want}:{stock}')#if the fruit is not available
    else:
        print(f"This fruit is in stock! \n We have stock of {stock} {fruit_want}")    
if __name__ == '__main__':
    main()
