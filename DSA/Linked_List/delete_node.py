class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
        
    def __str__(self):
        return f'Node {self.data}=> {self.next}'
        
def delete(node,location):
    ptr = node
    ptr2 = node.next
    while ptr2 !=None and ptr2.data != location:
        ptr2 = ptr2.next
        ptr = ptr.next     
    ptr.next = ptr2.next
    ptr2.next = None
    return node
    
    
n1 = Node(10,Node(20,Node(30,Node(40,Node(50,Node(60,Node(70,Node(80,Node(90)))))))))
print(delete(n1,int(input("Enter the node that you want to delete:\n"))))