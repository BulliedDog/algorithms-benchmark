class linkedList:
    def __init__(self, type):
        self.root = None
        self.size = 0
        self.type = type
        
    def insert(self, node):
        if self.size == 0:
            self.root = node
        else:
            lastNode = self._getLast()
            lastNode.next = node
        self.size += 1
    
    def _getLast(self):
        if self.size == 0:
            return None
        lastNode = self.root
        while lastNode.next is not None:
            lastNode = lastNode.next
        return lastNode
    
    def extract(self): # estrae il massimo o il minimo
        if self.size == 0:
            return None
        targetNode = self.root # nodo di appoggio max o min
        node = targetNode.next
        while node is not None:
            if (node.value > targetNode.value if self.type == "max" else node.value < targetNode.value):
                targetNode = node
        return node
    
    

class node:
    def __init__(self, value):
        self.value = value
        self.next = None