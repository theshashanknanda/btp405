file = open("sample.txt", "r")

myDict = {}

while True:
    c = file.read(1)
    if not c:
        break

    if c in myDict.keys():
        myDict[c] = myDict[c] + 1
    else:
        myDict[c] = 1

print(myDict)
