import random, gc
import matplotlib.pyplot as plt
from time import perf_counter as now
from data_structures import *
import pandas as pd
# NUMBER SET SIZES
numberOfIterations = 50 # for each number set size
numberSetSize = [100,200,500,1000,2000]
structureNames = ["Heap", "LinkedList", "LinkedOrderedList"]
constructors = {"Heap": Heap, "LinkedList": LinkedList, "LinkedOrderedList": LinkedOrderedList}
variations = ["max", "min"]
operations = ['Insert', 'IncDec', 'Extract'] #TODO: AGGIUNGERE ANCHE IMPLEMENTAZIONE RICERCA
maxValue = 10000
numberIncDecLimit = maxValue # volendo modificabile

# DATA STRUCTURES #
structures = {
    f'[variation->{v}][structure->{s}][dimension->{d}][iteration->{i}]': constructors[s](v,d,i) for v in variations for s in structureNames for d in numberSetSize for i in range(1, numberOfIterations + 1) 
}

# RANDOM NUMBERS DATASETS PER DIMENSION - all random #
numbers = {
    f'{name}': random.sample(range(0, maxValue), ds.plannedSize) for name, ds in structures.items()
}

# TIMING LISTS #
timingLists = {
    f'{v}{s}{d}{op}': [] for v in variations for s in structureNames for op in operations for d in numberSetSize # appende un tempo per ogni iterazione
}

# MEDIA TEMPI PER OPERAZIONE
meanTimingLists = {
    f"{v}{s}{op}": [] for v in variations for s in structureNames for op in operations
}

# INSERT #
print("Raccolta tempi insert:\n")
for name, ds in structures.items():
    elapsed = 0
    for n in numbers[f"{name}"]:
        gc.disable()
        start = now()
        ds.insert(n)
        end = now()
        gc.enable()
        elapsed += (end - start) * 1000 # ms * 1000 = ms
    check = getattr(ds, "checkOrder", None)
    if callable(check):
        check()
    timingLists[f"{ds.type}{ds.name}{ds.plannedSize}Insert"].append(elapsed)
    print(f"{name} => inseriti {len(numbers[f"{name}"])} elementi in {elapsed}ms")

# INCDEC VALORE #
print("Raccolta tempi inc/dec valore:\n")
for name, ds in structures.items():
    elapsed = 0
    for i in range(ds.size):
        randomIndex = random.randrange(ds.size)
        randomValue = random.randrange(0, numberIncDecLimit + 1)
        if ds.name == "Heap":
            value = ds.getValue(randomIndex)
            if ds.type == "max":
                value += randomValue
            else:
                value -= randomValue
        else:
            value = randomValue
        gc.disable()
        start = now()
        flag = ds.incDecValue(randomIndex, value)
        end = now()
        gc.enable()
        if flag == False:
            raise Exception(f"{name} -> errore (iterazione {i} nell'indice {randomIndex} fuori range, dimensione[{ds.size}] o struttura vuota!")
        elapsed += (end - start) * 1000
    check = getattr(ds, "checkOrder", None)
    if callable(check):
        check()
    timingLists[f"{ds.type}{ds.name}{ds.plannedSize}IncDec"].append(elapsed)
    print(f"{name} => cambiato valore di {ds.plannedSize} elementi in {elapsed}ms")

# EXTRACT #
print("Raccolta tempi extract valori max/min:\n")
for name,ds in structures.items():
    elapsed = 0
    for i in range(ds.plannedSize):
        gc.disable()
        start = now()
        node = ds.extract()
        end = now()
        gc.enable()
        if node is None:
            raise Exception(f"{name} -> errore durante l'estrazione {i}, la struttura è vuota!")
        elapsed += (end - start) * 1000 # ms * 1000 = ms
        check = getattr(ds, "checkOrder", None)
        if callable(check):
            check()
    timingLists[f"{ds.type}{ds.name}{ds.plannedSize}Extract"].append(elapsed)
    print(f"{name} => estratti {ds.plannedSize} elementi {ds.type} in {elapsed}ms")

for v in variations:
    for s in structureNames:
        for op in operations:
            for d in numberSetSize:
                mean = 0
                for time in timingLists[f"{v}{s}{d}{op}"]:
                    mean += time
                mean /= len(timingLists[f"{v}{s}{d}{op}"])
                meanTimingLists[f"{v}{s}{op}"].append(mean)

# GRAPH PLOTTING #
plt.style.use('dark_background')
for op in operations:
    plt.figure(figsize=(10, 7))
    for var in variations:
        for struct in structureNames:
            key = f"{var}{struct}{op}"
            label = f"{var} {struct}"
            if key in meanTimingLists:
                means = meanTimingLists[key]
                plt.plot(numberSetSize, means, marker='o', label=label)
    plt.title(f"Media tempi {op} per dimensione dataset")
    plt.xlabel("Dimensione dataset (n)")
    plt.ylabel("Tempo operazione (ms)")
    plt.legend()
    plt.grid(False)
    plt.savefig(f"graphs/{op.lower()}_timing_plot.png", facecolor='black', bbox_inches='tight')
#plt.show()

# TABELLA TEMPI ITERAZIONI #
rows = []
for name, time in timingLists.items():
    rows.append({
        "Tipo di struttura \n[variazione][struttura][dimensione][operazione]": name,
        **{f"Tempo (ms) iterazione {i+1}": t for i, t in enumerate(time)}
    })
df = pd.DataFrame(rows)
df.set_index("Tipo di struttura \n[variazione][struttura][dimensione][operazione]")
df.to_csv("tables/tabella_tempi_iterazioni.csv")

# TABELLA TEMPI MEDI #
rows = []
for name, time in meanTimingLists.items():
    rows.append({
        "Tipo di struttura \n[variazione][struttura][operazione]": name,
        **{f"Dimensione dataset {numberSetSize[i]}": t for i, t in enumerate(time)}
    })
df = pd.DataFrame(rows)
df.set_index("Tipo di struttura \n[variazione][struttura][operazione]")
df.to_csv("tables/tabella_tempi_medi.csv")