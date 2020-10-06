import random
import mytools
import sys
import time

def getRandomList(pool, numberCount):
    for i in range(0,numberCount):
        n = random.randint(minimum,maximum - 1) - minimum
        mytools.swap(pool, i, n)
        randomList = pool[:numberCount]
    return randomList

def config():
    global minimum
    global maximum
    global numberCount
    print("Geben Sie die Minimalzahl ein.")
    minimum = mytools.getNumber()
    maximum = minimum - 1
    maximum = maxZahl(maximum, minimum)
    rangeMinMax = maximum - minimum + 1
    numberCount = rangeMinMax + 1
    numberCount = rangeCount(rangeMinMax, numberCount)

def rangeCount(rangeMinMax, numberCount):
    while rangeMinMax < numberCount or numberCount <= 0:
        print("\nWie häufig soll gezogen werden?")
        numberCount = mytools.getNumber()
        if numberCount > rangeMinMax:
            print("\nDie Zahl darf nicht größer sein, als die Differenz von Maximalzahl und Minimalzahl.")
        if numberCount == 0:
            print("\nBei 0 findet keine Ziehung statt.")
            exiter()
    return numberCount

def maxZahl(maximum, minimum):
    while maximum <= minimum:
        print("\nGeben Sie die Maximalzahl ein.")
        maximum = mytools.getNumber()
        if maximum <= minimum:
            print("\nSie muss größer sein als die Minimalzahl.")
    return maximum

def exiter():
    exiter = input("\n0 zum Beenden des Zahlengenerators\nAny Key zum fortsetzen.\n")
    if (exiter == "0"):
        print("Das Programm wurde erfolgreich beendet.")
        sys.exit()
    else:
        return

def startGenerator():
    print("\n#####################################")
    print("## Willkommen beim Zahlengenerator ##")
    print("#####################################")
    exiter()
    config()
    pool = list(range(minimum, maximum + 1))
    randomList = getRandomList(pool, numberCount)
    print("#####################################")
    print("\nrandomList unsortiert:")
    print(randomList)
    print("\nrandomList sortiert mit BubbleSort (aufsteigend):")
    startTime = time.perf_counter()
    print(mytools.sortBubble(randomList, numberCount))
    endTime = time.perf_counter()
    timeBubbleAuf = endTime - startTime

    print("\nrandomList sortiert mit BubbleSort (absteigend):")
    startTime = time.perf_counter()
    print(mytools.sortBubble(randomList, numberCount)[::-1])
    endTime = time.perf_counter()
    timeBubbleAb = endTime - startTime

    print("\nrandomList sortiert mit SelectSort (aufsteigend):")
    startTime = time.perf_counter()
    print(mytools.sortSelect(randomList, numberCount))
    endTime = time.perf_counter()
    timeSortAuf = endTime - startTime

    print("\nrandomList sortiert mit SelectSort (absteigend):")
    startTime = time.perf_counter()
    print(mytools.sortSelect(randomList, numberCount)[::-1])
    endTime = time.perf_counter()
    timeSortAb = endTime - startTime

    print("\nrandomList sortiert mit Python built-in-sort (aufsteigend):")
    startTime = time.perf_counter()
    print(sorted(randomList))
    endTime = time.perf_counter()
    timeSortedAuf = endTime - startTime

    print("\nrandomList sortiert mit Python built-in-sorted (absteigend):\n")
    startTime = time.perf_counter()
    print(sorted(randomList, reverse=True))
    endTime = time.perf_counter()
    timeSortedAb = endTime - startTime

    print(f"Benötigte Zeit zum sortieren (BubbleSort Auf):      {timeBubbleAuf:0.9f} Sekunden")
    print(f"Benötigte Zeit zum sortieren (BubbleSort Ab):       {timeBubbleAb:0.9f} Sekunden")
    print(f"Benötigte Zeit zum sortieren (SelectSort Auf):      {timeSortAuf:0.9f} Sekunden")
    print(f"Benötigte Zeit zum sortieren (SelectSort Ab):       {timeSortAb:0.9f} Sekunden")
    print(f"Benötigte Zeit zum sortieren (built-in-sorted Auf): {timeSortedAuf:0.9f} Sekunden")
    print(f"Benötigte Zeit zum sortieren (built-in-sorted Ab):  {timeSortedAb:0.9f} Sekunden")

def main():
    while True:
        startGenerator()

if __name__ == "__main__":
    main()
