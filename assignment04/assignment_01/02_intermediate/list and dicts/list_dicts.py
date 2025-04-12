#list and dicts game
#Accessing Elements:
def access(lst):
    print("🔍 Access an element from the list")
    try:
        element_index = int(input("Enter the element index: "))#user input
        return f"Element at index {element_index}: {lst[element_index]}"#return
    except IndexError:
        return "❌ Index is out of range"#error
    except ValueError:
        return "❌ Enter a valid number"#error
#Modifying Elements:
def modify(lst):
    print("✏️ Modify an element in the list")
    try:
        element_input = input("Enter the new element: ")#user input
        replace_index = int(input("Enter the index to replace: "))#user input
        lst[replace_index] = element_input#replacing element
        return f"✅ Element updated. New list: {lst}"#returning response
    except IndexError:
        return "❌ Index is out of range"#error
    except ValueError:
        return "❌ Enter a valid number"#error
#Slicing the List:
def slices(lst):
    print("✂️ Slice a portion of the list")
    try:
        start_index = int(input("Enter start index: "))#user input
        end_index = int(input("Enter end index: "))#user input

        start_index = max(0, start_index)#slicting from index
        end_index = min(len(lst), end_index)#slicing till index

        if start_index >= end_index:
            return "⚠️ Invalid range. Nothing to slice."#error

        return f"Sliced list: {lst[start_index:end_index]}"#returning sliced list
    except ValueError:
        return "❌ Enter valid numbers"#error

def main():
    element_list = ['apple', 'banana', 'bag', 'suitcase', 43, 'shoes', 56]#list

    print("🎮 Welcome to the Game!")
    print(f"Current List: {element_list}")#printed the main list
    #list of functions
    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
    #user input to choose ay function
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            result = access(element_list)
            print(result)
        elif choice == '2':
            result = modify(element_list)
            print(result)
        elif choice == '3':
            result = slices(element_list)
            print(result)
        elif choice == '4':
            print("👋 Thanks for playing!")
            break
        else:
            print("❌ Invalid choice. Please choose 1, 2, 3, or 4.")#error

        print(f"📌 Current List: {element_list}")#printing list

if __name__ == '__main__':
    main()
