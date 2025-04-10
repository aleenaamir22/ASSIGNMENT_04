#PYTHAGOREAN THEOREM
#PROBLEM STATEMENT 
#Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!
import math

def main():
 
    AB=float(input('Enter the length of AB: '))
    AC=float(input('Enter the length of AC: '))
    BC=math.sqrt(AB**2 + AC**2)
    print(f'Hypotenuse (BC) = {BC}')

if __name__ == '__main__':
  main()   