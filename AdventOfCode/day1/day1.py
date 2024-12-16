firstList = []
secondList = []
secondListFreq = {}
with open('./input.txt','r') as file:
    for line in file:
        ele = line.split()
        firstList.append(int(ele[0]))
        secondList.append(int(ele[1]))
        if(int(ele[1]) not in secondListFreq):
            secondListFreq[int(ele[1])] = 1
        else:
            secondListFreq[int(ele[1])] = secondListFreq[int(ele[1])] + 1
firstList.sort()
secondList.sort()
#part 1
#sort both lists in ascending order to find the distance between two cooresponding coordinates
totalDist = 0

for i in range(len(firstList)):
    totalDist += abs(firstList[i] - secondList[i])

print(totalDist)

# part 2

totalSimilarity = 0
for ele in firstList:
    frequency = secondListFreq[ele] if ele in secondListFreq else 0
    totalSimilarity = totalSimilarity + (ele * frequency)

print(totalSimilarity)
