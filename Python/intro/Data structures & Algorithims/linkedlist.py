class Node():
    def __init__(self,value,next=None):
        self.value=value
        self.next=next

    def print_node(self):
        current=self
        print("Current Value", current.value)
        print("Has next", current.next)
        if current.next:
            print(current.next.__dict__)

c=Node(value=18,next=None)
b=Node(value=35,next=c)
a=Node(value=20,next=b)