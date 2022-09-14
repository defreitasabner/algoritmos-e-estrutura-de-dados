data = [94, 71, 0, 62, 48, 80]

for scanIndex in range(1, len(data)): 
    temp = data[scanIndex] 
    minIndex = scanIndex
    while minIndex > 0 and temp < data[minIndex - 1]: 
        data[minIndex] = data[minIndex - 1] 
        minIndex -= 1
        data[minIndex] = temp
    print(data)
    