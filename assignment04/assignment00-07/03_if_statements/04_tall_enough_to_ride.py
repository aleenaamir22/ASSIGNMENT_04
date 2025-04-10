def main():
    max_height=50 
    while True: #loop
     user_input=(input('Enter your height (like:10) or click enter to exit: '))#user input their height
     if user_input=="":
        break
     try:
            height = float(user_input)
            if height >= max_height:
                print("You are tall enough to ride this time 🎢!")
            else:
                print("You're not tall enough to ride this time 😔.")
     except ValueError:
            print("Please enter a valid number!")
if __name__ == '__main__':
     main()