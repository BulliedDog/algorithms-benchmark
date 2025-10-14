import sys, random, time
sys.path.append('../data structures')
import heap, linkedList, linkedOrderedList

### RANDOM NUMBER SET ###
numbers = random.sample(range(1, 10001), 1000)
#########################

### DATA STRUCTURES ###
structures = {
    'maxHeap': heap("max"),
    'minHeap': heap("min"),
    'maxLinkedList': linkedList("max"),
    'minLinkedList': linkedList("min"),
    'maxLinkedOrderedList': linkedOrderedList("max"),
    'minLinkedOrderedList': linkedOrderedList("min"),
}
#######################

### CREAZIONE LISTE TEMPI AUTOMATICA (prodotto cartesiano Struttura * Op) ###
operation_types = ['Insert', 'IncDec', 'Extract']
timing_lists = {f"{name}{op}Times": [] for name in structures for op in operation_types}
#############################################################################

### COLLEZIONE TEMPI TRASCORSI ###
for n in numbers:
        start = time.time()
        maxHeap.insert(n)
        end = time.time()
        maxHeapInsertTimes.append(end - start)
        start = time.time()
        minHeap.insert(n)
        end = time.time()
        maxHeapInsertTimes.append(end - start)
##################################

