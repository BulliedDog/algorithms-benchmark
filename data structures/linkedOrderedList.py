class linkeOrderedList:
    def __init__(self, type):
        self.root = None
        self.size = 0
        self.type = type
        
    def insert(self, node):
        if self.size == 0:
            self.root = node
        else:
            predecessorNode = self._getPredecessor()
            predecessorNode.next = node
        self.size += 1
    
    def _getPredecessor(self, value): # serve a cercare l'ultimo nodo più grande/piccolo di quello da inserire
        predecessorNode = self.root
        while predecessorNode.next is not None and (value < predecessorNode.next.value if self.type == "max" else value > predecessorNode.next.value):
            predecessorNode = predecessorNode.next
        return predecessorNode

    def extract(self): # estrae il massimo o il minimo che sarà sempre il primo elemento poiché la lista è ordinata
        if self.size == 0:
            return None
        targetNode = self.root
        if self.root.next is not None:
            self.root = self.root.next
        else:
            self.root = None
        return targetNode # estraendo il primo elemento la lista rimarrà sempre ordinata

    ### TODO: ADAPT
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