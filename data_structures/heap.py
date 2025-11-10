class Heap:
    def __init__(self, type: str, plannedSize: int, iteration: int):
        self.array = []
        self.type = type
        self.size = 0
        self.name = "Heap"
        self.iteration = iteration
        self.plannedSize = plannedSize
    def _heapify(self, i: int):
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

    def extract(self) -> int: # estrae il massimo/minimo
        if len(self.array) < 1:
            return None
        basket = self.array[0] # basket contiene o il max o il min
        self.array[0] = self.array[-1] # mette come primo elemento (max/min) il valore finale
        self.array.pop() # elimina l'elemento all'ultima posizione che sarebbe l'elemento massimo dopo lo scabio della riga sopra
        self._heapify(0)
        self.size -= 1
        return basket
    
    def incDecValue(self, i: int, value: int) -> bool: # incrementa/diminuisce il valore a seconda del tipo di heap
        if (value < self.array[i] if self.type == "max" else value > self.array[i]):
            return False # se il tipo è max/min il valore deve per forza essere maggiore/minore o uguale rispettivamente
        self.array[i] = value
        parent = (i - 1) // 2
        while i > 0 and (self.array[parent] < self.array[i] if self.type == "max" else self.array[parent] > self.array[i]):
            tmp = self.array[parent]
            self.array[parent] = self.array[i]
            self.array[i] = tmp
            i = parent
            parent = (i - 1) // 2
        return True
    
    def insert(self, value: int):
        self.array.append(value)
        self.incDecValue(len(self.array) - 1, value)
        self.size += 1

    def getValue(self, i: int) -> int:
        return self.array[i]
