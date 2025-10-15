import random, time
from data_structures import *

### RANDOM NUMBER SET ###
numbers = random.sample(range(0, 10000), 1000)
#########################

### DATA STRUCTURES ###
structures = {
    'maxHeap': Heap("max"),
    'minHeap': Heap("min"),

    'maxLinkedList': LinkedList("max"),
    'minLinkedList': LinkedList("min"),
    'maxLinkedOrderedList': LinkedOrderedList("max"),
    'minLinkedOrderedList': LinkedOrderedList("min"),
}
#######################

### OPERATIONS ###
operations = ['Insert', 'IncDec', 'Extract']

timingLists = {
    f"{name}{op}Times": [] for name in structures for op in operations
}

### insert ###
print("Test insert:\n")
i = 0
for n in numbers:
    for name, ds in structures.items():
        i += 1
        start = time.time()
        flag = ds.insert(n)
        end = time.time()
        elapsed = (end - start) * 1000 # s * 1000 = ms
        timingLists[f"{name}InsertTimes"].append(elapsed)
        if flag == False:
            raise(Exception(f""))
        print(f"{name} -> inserito valore = {n} iterazione = {i} in {elapsed}ms")
##############

### incDecValue ###
print("Test inc/dec valore:\n")
i = 0
for n in numbers:
    for name, ds in structures.items():
        i += 1
        randomIndex = random.randrange(0, ds.size - 1)
        randomValue = random.randrange(0, 1000)
        if name[3:7] == "Heap":
            value = ds.getValue(randomIndex)
            if name[0:3] == "max":
                value += randomValue
            else:
                value -= randomValue
        else: 
            value = randomValue
        start = time.time()
        flag = ds.incDecValue(randomIndex, value)
        end = time.time()
        if flag == False:
            raise Exception(f"{name} -> errore (iterazione {i} nell'indice {randomIndex} fuori range, dimensione[{ds.size}] o struttura vuota!")
        elapsed = (end - start) * 1000 # ms * 1000 = ms
        timingLists[f"{name}IncDecTimes"].append(elapsed)
        print(f"{name} -> cambiato valore = {value} iterazione = {i} in {elapsed}ms")
###################

### extract ###
print("Test extract valori max/min:\n")
i = 0
for n in numbers:
    for name,ds in structures.items():
        i += 1
        start = time.time()
        node = ds.extract()
        end = time.time()
        elapsed = (end - start) * 1000 # ms * 1000 = ms
        timingLists[f"{name}ExtractTimes"].append(elapsed)
        if node is None:
            raise Exception(f"{name} -> errore durante l'estrazione {i}, la struttura è vuota!")
        else:
            print(f"{name} -> estratto nodo {(node if isinstance(node, int) else node.value)} iterazione = {i} in {elapsed}ms")
###############