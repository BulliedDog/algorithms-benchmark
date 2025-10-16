import random, time
from tabulate import tabulate
import matplotlib.pyplot as plt
from data_structures import *
import pandas as pd

### RANDOM NUMBER SET ###
while True:
    numberSetSize = int(input("Inserire il numero di dati randomici da testare [default = 1000]-> ") or 1000)
    if numberSetSize > 0:
        break
numbers = random.sample(range(0, int(input("Inserire il valore massimo dei numeri [default = 1000]-> ") or 1000)), numberSetSize)
numberIncDecLimit = int(input("Inserire il valore massimo di incremento/decremento [default = 1000]-> ") or 1000)
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
##################

### TIMING LISTS ###
timingLists = {
    f"{name}{op}Times": [] for name in structures for op in operations
}

sumTimingLists = {
    f"{name}{op}Times": [] for name in structures for op in operations
}
####################

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
        randomIndex = random.randrange(0, numberSetSize)
        randomValue = random.randrange(0, numberIncDecLimit)
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

### CALCULATING THE TOTAL TIME PER ITERATION ###
for op in operations:
    for name, ds in structures.items():
        prev = 0
        for t in timingLists[f"{name}{op}Times"]:
            current = t # copia per valore dato che int è una variabile immutabile
            current += prev
            prev = current
            sumTimingLists[f"{name}{op}Times"].append(current)
################################################

### SAVING CSV FILE ###
# IN THE "timingLists_combaned.csv" file, format is the following #
# LEFT TABLE -> SINGLE TIME TABLE # 
# RIGHT TABLE -> SUM TIME TABLE #
timing_df = pd.DataFrame(timingLists)
sum_timing_df = pd.DataFrame(sumTimingLists)

max_len = max(len(timing_df), len(sum_timing_df))
timing_df = timing_df.reindex(range(max_len))
sum_timing_df = sum_timing_df.reindex(range(max_len))

timing_df.insert(0, "Iteration", range(1, max_len + 1))
sum_timing_df.insert(0, "Iteration", range(1, max_len + 1))

blank_col = pd.Series([""] * max_len, name="")

combined_df = pd.concat(
    [timing_df, blank_col, sum_timing_df.drop(columns="Iteration")],
    axis=1
)

combined_df.to_csv("tables/timingLists_combined.csv", index=False)
########################

### GRAPHS AND PLOTTING ###
plt.style.use("dark_background")
for op in operations:
    plt.figure(figsize=(10, 6))
    for name in structures:
        times = sumTimingLists[f"{name}{op}Times"]
        plt.plot(times, label=f"{name} {op}")
    plt.xlabel("Iterazioni")
    plt.ylabel("Tempo (ms)")
    plt.title(f"Tempi di {op} dati per ogni struttura")
    plt.legend()
    plt.savefig(f"graphs/{name}{op}TotalTimes.png")
    plt.get_current_fig_manager().set_window_title(f"Grafico Tempi Totali")

for op in operations:
    plt.figure(figsize=(10, 6))
    for name in structures:
        times = timingLists[f"{name}{op}Times"]
        plt.bar(range(len(times)), times, label=f"{name} {op}", alpha=0.7, width=1)
    plt.xlabel("Iterazioni")
    plt.ylabel("Tempo (ms)")
    plt.title(f"Tempi di {op} dati per ogni struttura")
    plt.legend()
    plt.savefig(f"graphs/{name}{op}SingleTimes.png")
    plt.get_current_fig_manager().set_window_title(f"Grafico Tempi Singoli")

plt.show()
############################