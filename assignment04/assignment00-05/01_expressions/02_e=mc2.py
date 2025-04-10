#Problem statement
#Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula

def main():

    c=299792458 
    mass=float(input('Enter the mass:'))

    energy=(mass*c**2)
    
    print("Formula:e=mc^2 ")
    print(f'Mass = {mass}kg')
    print(f'c={c}m/s')
    print(f'The Energy is = {energy}Joules ')


if __name__ == '__main__':
      main()    