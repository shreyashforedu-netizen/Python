stack = []
MAX = 5

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if len(stack) == MAX:
            print("Stack Overflow")
        else:
            value = int(input("Enter element: "))
            stack.append(value)
            print("Element pushed successfully")

    elif choice == 2:
        if len(stack) == 0:
            print("Stack Underflow")
        else:
            print("Popped element:", stack.pop())

    elif choice == 3:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Stack elements:", stack[::-1])

    elif choice == 4:
        break

    else:
        print("Invalid choice")
