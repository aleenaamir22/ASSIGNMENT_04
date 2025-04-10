#shorten list

def remove(list):
 Maximum_length = 3  #max length
 while len(list) > Maximum_length: #loop
   remove_elements=list.pop()#removing operation
   print(f'Remove elements: {remove_elements}')#response of removed elements

def main():
  list=[1,2,3,4,5,6] #list of elements
  remove(list)  #calling removing func
  print(f'List: {list}') #response of printing the remaining elemments in the list

if __name__ == '__main__':
   main()