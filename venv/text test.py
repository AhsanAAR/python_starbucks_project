listOfAttr = []
foHeights = open("Records.txt", "r")
for line in foHeights:
    listOfAttr.append(line.split('!'))

print(listOfAttr)