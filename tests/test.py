import sys, random, time
sys.path.append('../data structures')
import heap, linkedList, linkedOrderedList

numbers = random.sample(range(1, 10001), 1000)

maxHeap = heap("max")
minHeap = heap("min")
maxLinkedList = linkedList("max")
minLinkedList = linkedList("min")
maxLinkedOrderedList = linkedOrderedList("max")
minLinkedOrderedList = linkedOrderedList("min")

for n in numbers:
    start = time.time()

    end = time.time()
    duration = end - start


