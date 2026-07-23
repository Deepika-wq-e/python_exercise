class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
        print(f"{item} pushed to stack")
    def pop(self):
        if self.is_empty():
            return "Stack Underflow"
        return self.stack.pop()
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]
    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)
    def display(self):
        print("stack Books:",self.stack)
s=Stack()
while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Size")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            value = input("Enter Book name to push: ")
            s.push(value)
            print("Book pushed successfully.")
        case 2:
            result = s.pop()
            if result is None:
                print("Stack is empty.")
            else:
                print("Popped:", result)
        case 3:
            result = s.peek()
            if result is None:
                print("Stack is empty.")
            else:
                print("Top Book:", result)
        case 4:
            print(" Display:", s.display())
        case 5:
            print("Size Of the Books:",s.size())
        case 6:
            print("Exiting...")
            break
        case _:
            print("Invalid choice!")
