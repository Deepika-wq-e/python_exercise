class Node:
    def __init__(self,coeff,exp):
        self.coeff=coeff
        self.exp=exp
        self.next=None
class Polynomial:
    def __init__(self):
        self.head=None
    def insert(self,coeff,exp):
        new_node=Node(coeff,exp)
        if not self.head or self.head.exp<exp:
            new_node.next=self.head
            self.head=new_node
            return
        temp=self.head
        while temp.next and temp.next.exp>exp:
            temp=temp.next
        if temp.exp==exp:
            temp.coeff+=coeff
        else:
            new_node.next=temp.next
            temp.next=new_node
    def add(poly1,poly2):
        m=poly1.head
        d=poly2.head
        res=Polynomial()
        while m and d:
            if m.exp==d.exp:
                res.insert(m.coeff+d.coeff,m.exp)
                m=m.next
                d=d.next
            elif m.exp>d.exp:
                res.insert(m.coeff,m.exp)
                m = m.next
            else:
                res.insert(d.coeff,d.exp)
                d = d.next
        while m:
            res.insert(m.coeff,m.exp)
            m=m.next
        while d:
            res.insert(d.coeff,d.exp)
            d=d.next
        return res
    def display(self):
        if self.head is None:
            print("0")
            return
        temp=self.head
        while temp:
            print(f"{temp.coeff}x^{temp.exp}",end=" ")
            if temp.next:
                print("+",end=" ")
            temp=temp.next
        print()
poly1=Polynomial()
poly2=Polynomial()
n1=int(input("Enter number of terms in the first polynomial:"))
n2=int(input("Enter number of terms in the second polynomial:"))
for i in range(n1):
    c=int(input("Enter coefficient:"))
    e=int(input("Enter power:"))
    poly1.insert(c,e)
for i in range(n2):
    c=int(input("Enter coefficient:"))
    e=int(input("Enter power:"))
    poly2.insert(c,e)
print("polynomial:")
poly1.display()
poly2.display()
sum = Polynomial.add(poly1,poly2)
sum.display()
