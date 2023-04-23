class Node:
    def __init__(self,data,next=None):
        self.data= data
        self.next = next
    def __str__(self):
        return f'Node{self.data}=> {self.next}'

def insert_before(node,data,location):
    new_node = Node(data)
    while node.next.data != location:
        node = node.next
    new_node.next = node.next 
    node.next = new_node
    return node

start = Node(100,Node(200,Node(300,Node(400,Node(500)))))

insert_before(start,69,200)
print(start)