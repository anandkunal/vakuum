# An implementation of a queue using the methods of a stack and a list

class S:
    """ A very basic and intuitive stack that really only
        boasts pushing, popping, and some basic utility methods. 
        Note, I did not want to leverage the list's pop/push methods. """
    
    def __init__(self):
        self.stack = []
        
    def push(self, value):
        self.stack.insert(0, value)
        
    def pop(self):
        if len(self.stack) > 0:
            top = self.stack[0]
            self.stack.__delitem__(0)
            return top
        return None
    
    def __len__(self):
        return len(self.stack)
        
    def __str__(self):
        return str(self.stack)

        
class Q:
    """ A really simple queue - there are no explicit deletions. 
        All augmentations to the underlying data structure use stack methods. 
        We only need to adjust either the enqueue or the dequeue - I 
        picked the former."""
    
    def __init__(self):
        self.stack = S()
    
    def enqueue(self, value):
        temp = []
        while len(self.stack) > 0: temp.append(self.stack.pop())
        self.stack.push(value)
        for i in temp[::-1]: self.stack.push(i)
    
    def dequeue(self):
        return self.stack.pop()

    def __str__(self):
        return str(self.stack)

q = Q()

print q.dequeue()

q.enqueue(1)
q.enqueue(2)

print q.dequeue()

q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print q.dequeue()
print q.dequeue()

q.enqueue(6)

print q