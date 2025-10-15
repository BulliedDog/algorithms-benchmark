class LinkedOrderedList:
    def __init__(self, type):
        self.root = None
        self.size = 0
        self.type = type
        
    def insert(self, value):
        node = Node(value)
        if self.size == 0:
            self.root = node
        elif (node.value > self.root.value if self.type == "max" else node.value < self.root.value):
            node.next = self.root
            self.root = node
        else:
            predecessorNode = self._getPredecessor(node.value)
            node.next = predecessorNode.next
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
        self.size -= 1
        return targetNode # estraendo il primo elemento la lista rimarrà sempre ordinata

    def incDecValue(self, i, value): # quando cambio il valore a un singolo nodo basta che riordini quest'ultimo e non l'intera lista
        if i < 0 or i >= self.size or self.size == 0:
            return False
        predecessorNode = None # puntatore predecessore per lo scorrimento
        node = self.root # puntatore nodo scorrimento
        while node is not None and i > 0:
            predecessorNode = node
            node = node.next
        if predecessorNode is not None:
            predecessorNode.next = node.next  # remove node from current position
        else:
            self.root = node.next            # remove head
        node.value = value
        if self.root is None or (node.value > self.root.value if self.type == "max" else node.value < self.root.value):
            node.next = self.root
            self.root = node
        else:
            predecessorNewNode = self._getPredecessor(value)
            node.next = predecessorNewNode.next
            predecessorNewNode.next = node
        return True

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None