#double list
#Write a program that doubles each element in a list of numbers.

def main():
     numbers = [1,2,3,4,5]
     double = []

     for i in numbers:
            double.append(i * 2)
     print("Doubled list:" , double)
            


if __name__ =='__main__':
        main()