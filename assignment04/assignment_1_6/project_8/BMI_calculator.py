#BMI calculator

def main():

    user_input_weight=float(input('Enter your weight in kilogram: '))#user input his weight
    user_input_height=float(input('Enter your height in meters: '))#user input his height

    BMI= user_input_weight / (user_input_height **2)#calculating bmi

    print(f"Your BMI is:{BMI:.2f}")#printing response

if __name__ == '__main__':
    main()

