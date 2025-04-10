#Problem Statement 05
#Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

#float 
def main():
    #The user to enter the length
    FirstSide=float(input('Enter the length of first side of triangle:'))#length of first side
    SecondSide=float(input('Enter the length of first side of triangle:'))#length of Second side
    ThirdSide=float(input('Enter the length of first side of triangle:'))#length of Third side
    
    sum = FirstSide +  SecondSide + ThirdSide #sum of all three sides

    print(f'The perimeter of three sides of the triangle is {sum}')

if __name__ == '__main__':
    main()

#integer

def main():
    #The user to enter the length
    FirstSide=int(input('Enter the length of first side of triangle in integer:'))
    SecondSide=int(input('Enter the length of first side of triangle in integer:'))
    ThirdSide=int(input('Enter the length of first side of triangle in integer:'))
    sum = FirstSide +  SecondSide + ThirdSide

    print(f'The perimeter of three sides of the triangle is {sum}')

if __name__ == '__main__':
    main()    