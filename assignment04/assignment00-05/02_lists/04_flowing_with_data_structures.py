#floeing with data structure

def main():
      message = input('Enter your message: ') #user input
      list=[] #empty list

      print(f'List before: {list}')

      for _ in range(3): #loop
       list.append([message])
      
      print(f'List after:{list}') #list after modification
if __name__ == '__main__':
    main()