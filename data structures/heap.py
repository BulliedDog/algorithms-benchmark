class heap:
    def __init__(self,type):
        self.array = []
        self.type = type
    def _heapify(self, i):
        l = i*2+1 # figlio sinistro considerando i che parte da zero
        r = i*2+2 # figlio destro
        basket = i # cestello che contiene indice max/min da scambiare
        if l < len(self.array) and (self.array[l].value > self.array[i].value if self.type == "max" else self.array[l].value < self.array[i].value):
            basket = l # massimo attuale
        if r < len(self.array) and (self.array[r].value > self.array[basket].value if self.type == "max" else self.array[r].value < self.array[basket].value):
            basket = r
        if basket != i:
            tmp = self.array[i]
            self.array[i] = self.array[basket]
            self.array[basket] = tmp
            self._heapify(basket)

    def insert(self, node):
        self.array.append(node)


    def get(self): # only returns root, whether max or min
        return self.root
    def extract(self, index): # estrae il massimo/minimo
        if len(self.array) < 1:
            return None
        basket = self.array[0] # basket contiene o il max o il min
        self.array[0] = self.array[len(self.array)-1]
        self.array[len(self.array)-1] = None
        self._heapify(0)
        return basket

    def navigate(self, index):
        if index > self.size:
            return None
    def getLastSpot(self, node):
        if node == None:
            return None
        if node.left == None:

        getLast(node.left)
        getLast(node.right)