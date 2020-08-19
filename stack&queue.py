"""
This is a stack(LIFO) and queue(FIFO) implementation
"""

class stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if len(self.items) is None:
            print("UNDERFLOW")
        else:
            self.items.pop()


    def print_list(self):
        print(self.items)

s = stack()
s.pop()

#s.print_list()
s.pop()
s.print_list()