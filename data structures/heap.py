class heap:
    def __init__(self):
        self.root = None # radice dell'albero, se è max-heap -> elemento massimo, se è min-heap -> elemento minimo
        self.type = None # a seconda del valore di self.type, si comporterà come un max-heap o un min-heap
        self.size = 0
    def heapify(self, node):
        
    def insert(self, node):
        if self.root is None:
            self.root = node
            
    def get(self): # only returns root, whether max or min
        return self.root
    def extract(self, index): # extracts the max or min depending on the self.type, then hipifies 

    def navigate(self, index):
        if index > self.size:
            return None
    def getLast(self):
        
class node:
    def __init__(self,value):
        self.value = value
        self.index = None # probabilmente non serve nemmeno
        self.parent = None
        self.left = None
        self.right = None