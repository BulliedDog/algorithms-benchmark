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
            if lastNode is None:
                return False
            lastNode.next = node
        self.size += 1
    
    def _getLast(self, i=0):
        if self.size == 0:
            return None
        lastNode = self.root
        while lastNode.next is not None:
            lastNode = lastNode.next
        return lastNode
    
    def _getNode(self, i):
        if self.size == 0:
            return None
        targetNode = self.root
        while targetNode is not None and i > 0:
            targetNode = targetNode.next
            i -= 1
        return targetNode
        
    ### TODO: FIX THE EXTRACTION, YOU ARE ONLY RETURNING A REFERENCE
    def extract(self): # estrae il massimo o il minimo
        if self.size == 0:
            return None
        targetNode = self.root # nodo di appoggio max o min
        node = targetNode.next
        while node is not None:
            if (node.value > targetNode.value if self.type == "max" else node.value < targetNode.value):
                targetNode = node
        self.size -= 1
        return node
    
    def changeValue(self, i, value):
        if i < 0:
            return False
        targetNode = self._getNode(i)
        if targetNode is None:
            return False
        targetNode.value = value
        return True

class node:
    def __init__(self, value):
        self.value = value
        self.next = None