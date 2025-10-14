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
    ### TODO: COPIED, CHECK IF NECESSARY OR MODIFY TO ADAPT
    def _getLast(self, i=0):
        if self.size == 0:
            return None
        lastNode = self.root
        while lastNode.next is not None:
            lastNode = lastNode.next
        return lastNode
    
    ### TODO: MAKE IT POSSIBLE THAT THE NODE GETS POPPED AND THE LIST REORDERS ITSELF
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
        targetNode = self.root # nodo di appoggio max o min
        node = targetNode.next
        while node is not None:
            if (node.value > targetNode.value if self.type == "max" else node.value < targetNode.value):
                targetNode = node
        self.size -= 1
        return node
    
    def _popNode(self, predecessorNode, node):

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