def getNumber():
    while True:
        try:
            n = input("Bitte eine Ganzzahl eingeben: ")
            n = int(n)
            break
        except ValueError:
            print("Falsche Eingabe. Bitte nochmal versuchen.")
    return n

def swap(array, a, b):
    array[a], array[b] = array[b], array[a]
    return array

def sortBubble(array, count):
    for i in range(0,count):
        for j in range(count - 1 - i):
            if array[j] > array[j + 1]:
                swap(array, j, j + 1)
    return array

def sortSelect(array, count):
    for i in range(0,count):
        m = array[i]
        for j in range(0,count):
            if array[j] > m:
                m = array[j]
                swap(array, i, j)
    return array
