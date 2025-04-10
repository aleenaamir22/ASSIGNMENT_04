#Implement the following function which takes in 3 integers as parameters: Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low

def print_range(num,low,high):#function req
    if low<= num <=high:#condition
         return True
    else:
        return False
    
def main():
    #user inputs 
    num=int(input('Enter a number: '))
    low=int(input('Enter the lower range: '))
    high=int(input('Enter the higher range: ')) 
    #response printing
    if print_range(num,low,high):
        print(f"{num} is between the range of {low} & {high}") 
    else:
         print(f"{num} is not in between the range of {low} & {high}")     
if __name__ == '__main__':
    main()    