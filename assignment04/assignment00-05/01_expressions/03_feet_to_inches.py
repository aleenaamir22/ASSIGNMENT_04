#Problem statement
#Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

def main():
    inches_per_foot = 12  # 1 foot = 12 inches
    feet = float(input('Enter your feet: '))
    inches = feet * inches_per_foot

    print(f'By converting {feet} foot{"s" if feet != 1 else ""} into inches, your answer will be {inches} inches.')

if __name__ == '__main__':
    main()
 