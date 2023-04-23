class Node:
    
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
    def __str__(self):
        return f'Node:{self.data} => {self.next}'
        
n1 = Node(10,Node(20,Node(30,Node(40,Node(50)))))

print(n1)