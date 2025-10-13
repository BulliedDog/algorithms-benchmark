class linkedList:
    def __init__(self,):
        self.root = None
        self.size = 0
    
    def insert(self, node):
        if self.size == 0:
            self.root = node
            self.size += 1
        else:
            lastNode = self._getLast()

    def _getLast(self):
        if self.root is None:
            return None
        else:
            
        
class node:
    def __init__(self, value):
        self.value = value
        self.next = None