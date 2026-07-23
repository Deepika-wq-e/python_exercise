class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self,size):
        self.top=None
        self.size=size
        self.count=0
    def push(self,value):
        if self.count==self.size:
            print("Stack overflow")
            return
        new_node=Node(value)
        new_node.next=self.top
        self.top=new_node
        self.count+=1
        print(value,"pushed")
    def pop(self):
        if self.top is None:
            print("Stack overflow")
            return
        value=self.top.data
        self.top=self.top.next
        self.count-=1
        print(value,"popped")
    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element:",self.top.data)
    def display(self):
        if self.top is None:
            print("Stack is empty")
            return
        temp=self.top
        print("Stack elements:")
        while temp:
            print(temp.data)
            temp=temp.next
size=int(input("Enter stack size:"))
stack=stack(size)
print("\n __stack functions__")
print("1.push")
print("2.pop")
print("3.peek")
print("4.display")
print("5.exit")
while True:
    choice=int(input("enter your choice"))
    if choice==1:
        value = int(input("enter value"))
        stack.push(value)
    elif choice==2:
        stack.pop()    
    elif choice==3:
        stack.peek()
    elif choice==4:
        stack.display()
    elif choice==5:
        print("exiting....")
        break
    else:
        print("Invalid choice")
