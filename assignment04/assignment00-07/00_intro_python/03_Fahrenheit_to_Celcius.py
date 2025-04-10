#problem statement 03
#Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.
def main():
    
    #user input
    Fahrenheit=float(input('Enter your temperature in Fahrenheit: '))
    #conversion
    celcius=(Fahrenheit - 32) * 5.0 / 9.0

    #result
    print(f'Your temperature {Fahrenheit}°F = {celcius}°C')
if __name__ == '__main__':
    main()   