#Fibonacci sequence
#in fibonnaci we see a pattern that first term is added to the next term to make term after next 
#for eg:(0,1,1,2,3,5,8,13,21) in this we se by adding 0 and 1 the next term will be 1 and when we add 1 + 1 we get term after next 2 and when we add 1 + 2 we get 3 and similarly so on 
#Write a program to print terms in the Fibonacci sequence up to a maximum value.
#maximum term is 10,000

def main():

    maximum_value=10000 #max value as given in problem statement
    first_term=0 #initial term
    second_term=1 #next term

    while first_term <= maximum_value: #loop
        print(first_term , end=" ")#response
        next_term = (first_term + second_term) #addition to get next term
        first_term = second_term
        second_term = next_term
     
if __name__ == '__main__':
    main()
        