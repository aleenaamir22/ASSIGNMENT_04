#international voting age
#Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.

def main():
    #fictional countries and their voting age
    Peturksbouipo = 16
    Stanlau = 25
    Mayengua = 48
    #user input
    voting_age = int(input('Enter your age: '))

    if voting_age >= Peturksbouipo:
        print(f'You can vote in Peturksbouipo where the voting age is {Peturksbouipo}')#if cond is true
    else:
        print("You cannot vote in Peturksbouipo because yo are underage")
        #if cond is false

    if voting_age >= Stanlau:
        print(f'You can vote in Stanlau wher the voting age is {Stanlau}')#if cond is true
    else:
        print("You cannot vote in Stanlu because you are underage")#if cond is false

    if voting_age >= Mayengua:
        print(f'You can vote in Mayengua where voting age is {Mayengua}')   #condition true
    else:
        print("You cannot vote in Mayengua because you are underage")      #condition false       


if __name__ == '__main__':
    main()    