import random, time
from data_structures import heap as h, linkedList as l, linkedOrderedList as lo

### RANDOM NUMBER SET ###
numbers = random.sample(range(0, 10000), 1000)
#########################

### DATA STRUCTURES ###
structures = {
    'maxHeap': h.heap("max"),
    'minHeap': h.heap("min"),

    'maxLinkedList': l.linkedList("max"),
    'minLinkedList': l.linkedList("min"),
    'maxLinkedOrderedList': lo.linkedOrderedList("max"),
    'minLinkedOrderedList': lo.linkedOrderedList("min"),
}
#######################

### OPERATIONS ###
operations = ['Insert', 'IncDec', 'Extract']

timingLists = {
    f"{name}{op}Times": [] for name in structures for op in operations
}

### insert ###
print("Test insert:\n")
for n in numbers:
    for name, ds in structures.items():
        start = time.time()
        ds.insert(n)
        end = time.time()
        elapsed = (end - start) * 1000 # s * 1000 = ms
        timingLists[f"{name}InsertTimes"].append(elapsed)
        print(f"{name} -> inserito valore {n} in {elapsed}s")
##############

### incDecValue ###
print("Test inc/dec valore:\n")
i = 0
for n in numbers:
    for name, ds in structures.items():
        i += 1
        randomIndex = random(0, ds.size - 1)
        randomValue = random.randrange(0, 1000)
        if name[3:6] == "Heap":
            value = ds.getValue(randomIndex)
            if name[0:2] == "max":
                value += randomValue
            else:
                value -= randomValue
        else: 
            value = randomValue
        start = time.time()
        flag = ds.incDecValue(randomIndex, randomValue)
        end = time.time()
        if flag == False:
            raise Exception(f"{name} -> errore (iterazione {i} nell'indice fuori range o struttura vuota!")
        elapsed = (end - start) * 1000 # s * 1000 = ms
        timingLists[f"{name}IncDecTimes"].append(elapsed)
        print(f"{name} -> cambiato valore = {value} in {elapsed}s")
###################

### extract ###
print("Test extract valori max/min:\n")
i = 0
for n in numbers:
    for name,ds in structures:
        i += 1
        start = time.time()
        node = ds.extract()
        end = time.end()
        if node is None:
            raise Exception(f"{name} -> errore durante l'estrazione {i}, la struttura è vuota!")
        else:
            print(f"{name} -> estratto nodo {(node if isinstance(node, int) else node.value)}")
        
###############