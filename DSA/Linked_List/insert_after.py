class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return f'Node: {self.data} => {self.next}'
        
def add_after(node,data,location):
    new_node = Node(data)
    while node.data!= location:
        node = node.next
    new_node.next = node.next
    node.next = new_node
    return node
    
if __name__ =="__main__":

    n1 = Node(10,Node(20,Node(30,Node(40,Node(50)))))
    
    add_after(n1,90,40)
    print(n1)
    