class heap:
    def __init__(self):
        self.root = None # radice dell'albero, se è max-heap -> elemento massimo, se è min-heap -> elemento minimo
        self.type = None # a seconda del valore di self.type, si comporterà come un max-heap o un min-heap
    def heapify(self):

    def insert(self, nodo): 
        
    def get(self): # only returns root, whether max or min
        return self.root
    def extract(self, index): #extracts the max or min depending on the self.type, then hipifies 

class node:
    def __init__(self,value):
        self.value = value
        self.index = None
        self.parent = None
        self.left = None
        self.right = None