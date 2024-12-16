firstList = []
secondList = []
with open('./input.txt','r') as file:
    for line in file:
        ele = line.split()
        firstList.append(int(ele[0]))
        secondList.append(int(ele[1]))

firstList.sort()
secondList.sort()

totalDist = 0

for i in range(len(firstList)):
    totalDist += abs(firstList[i] - secondList[i])

print(totalDist)
