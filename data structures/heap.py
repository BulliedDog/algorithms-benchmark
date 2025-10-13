class heap:

    def __init__(self,type):
        self.array = []
        self.type = type

    def _heapify(self, i):
        l = i * 2 + 1 # figlio sinistro considerando i che parte da zero
        r = i * 2 + 2 # figlio destro
        basket = i # cestello che contiene indice max/min da scambiare
        if l < len(self.array) and (self.array[l] > self.array[i] if self.type == "max" else self.array[l] < self.array[i]):
            basket = l # massimo attuale
        if r < len(self.array) and (self.array[r] > self.array[basket] if self.type == "max" else self.array[r] < self.array[basket]):
            basket = r
        if basket != i:
            tmp = self.array[i]
            self.array[i] = self.array[basket]
            self.array[basket] = tmp
            self._heapify(basket)

    def extract(self, index): # estrae il massimo/minimo
        if len(self.array) < 1:
            return None
        basket = self.array[0] # basket contiene o il max o il min
        self.array[0] = self.array[len(self.array)-1]
        self.array[len(self.array)-1] = None
        self._heapify(0)
        return basket
    
    def changeValue(self, i, value): # incrementa/diminuisce il valore a seconda del tipo di heap
        if (value < self.array[i] if self.type == "max" else value > self.array[i]):
            return False
        self.array[i] = value
        if i % 2 != 0:  # se i % 2 = 0.5 allora il padre ha parte intera inferiore di i / 2, se è zero il padre è i / 2 - 1
            parent = i // 2
        else:
            parent = i / 2 - 1 
        while i > 1 and (self.array[parent] < self.array[i] if self.type == "max" else self.array[parent] > self.array[i]):
            tmp = self.array[]
    def insert(self, node):
        self.array.append(node)