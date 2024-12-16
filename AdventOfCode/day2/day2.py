reports = []
with open('./input.txt','r') as file:
    for line in file:
        reportLine = line.split()
        reports.append([int(ele) for ele in reportLine])

numSafeReports = 0

# part 1

for report in reports:
    reportOrder = 'increasing' if report[1] > report[0] else 'decreasing'
    safeReport = True
    for i in range(1,len(report)):
        if(abs(report[i] - report[i-1]) > 3 or report[i] == report[i-1]):
            safeReport = False
            break
        if(reportOrder == 'increasing' and report[i] < report[i-1]):
            safeReport = False
            break
        elif(reportOrder == 'decreasing' and report[i] > report[i-1]):
            safeReport = False
            break

    if(safeReport):
        numSafeReports = numSafeReports + 1

print(numSafeReports)
