# A minimal stack calculator that only supports addition/multipliction

class Stacker(object):
    def __init__(self):
        self.s = []
        self.ops = {
            '+' : lambda: self.s.append(self.s.pop() + self.s.pop()),
            '*' : lambda: self.s.append(self.s.pop() * self.s.pop())
        }
    
    def parse(self, source):
        tokens = source.split()
        for token in tokens:
            try:
                self.s.append(int(token))
            except ValueError:
                # Most likely an operator, check existence
                if token in self.ops:
                    self.ops[token]()
    
    def __str__(self):
        return str(self.s)

s = Stacker()
s.parse("18 3 + 2 * 1 +")
print s