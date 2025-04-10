def main(): 
     phone_book = {}

     print("\033[1m\033[3m Welcome to the PhoneBook📙 Created By Aleena \033[0m")#title msg
     while True:
          name = input('Enter name: ')#user input
          if name == "":
               break #on just pressing enter it will exit
          
          phone_number = input('Enter📙 number: ')#user input
          phone_book[name] = phone_number
          print(f'{name} added with phone number {phone_number}')#saving name and number
         
          print("Search Saved Contacts") #finding contact from phone book
          search=input('Enter name: ') #entering name to find out
          if search in phone_book:
               print(f'{search} : {phone_book[search]}') #if found than num will be printed with number
          else:
               print("Sorry,Not Found") #otherwise this msg of not finding contact
               break   #than exit from the phone book
            
if __name__ == '__main__':
     main() 