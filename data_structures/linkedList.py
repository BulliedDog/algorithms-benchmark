class LinkedList:
    def __init__(self, type):
        self.root = None
        self.size = 0
        self.type = type
        
    def insert(self, value):
        node = Node(value)
        if self.size == 0:
            self.root = node
        else:
            lastNode = self._getLast()
            if lastNode is None:
                return False
            lastNode.next = node
        self.size += 1
    
    def _getLast(self):
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
        
    def extract(self): # estrae il massimo o il minimo
        if self.size == 0:
            return None
        predecessorTargetNode = None
        targetNode = self.root # nodo di appoggio max o min
        predecessorNode = None
        node = targetNode.next
        while node is not None:
            if (node.value > targetNode.value if self.type == "max" else node.value < targetNode.value):
                predecessorTargetNode = predecessorNode
                targetNode = node
            predecessorNode = node
            node = node.next
        if predecessorTargetNode is not None:
            predecessorTargetNode.next = targetNode.next
        else:
            self.root = targetNode.next
        self.size -= 1
        return targetNode
    
    def incDecValue(self, i, value): # non necessita alcun controllo sui valori (maggiore dell'attuale se max, minore se min) perché è disordinata la lista
        if i < 0 or i >= self.size or self.size == 0:
            return False
        targetNode = self._getNode(i)
        if targetNode is None:
            return False
        targetNode.value = value
        return True

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None