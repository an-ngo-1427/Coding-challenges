def romanToInt(s):
    romanDict = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    sum = 0
    prev = ''

    for i in range(len(s)):
        print(i,sum,s[i],prev)
        if(len(prev) == 0):
            if(s[i] == 'I'):
                prev = s[i]
                sum += 1
                continue
            if(s[i] == 'X'):
                prev = s[i]
                sum += 10
                continue
            if(s[i] == 'C'):
                prev = s[i]
                sum += 100
                continue
        if((s[i] == 'V' or s[i] == 'X') and prev == 'I'):
            sum += (romanDict[s[i]] - 2)
            prev = ''
            continue
        if((s[i] == 'L' or s[i] == 'C') and prev == 'X'):
            sum += (romanDict[s[i]] - 20)
            prev = ''
            print('inside if',romanDict[s[i]] - 20)
            continue
        if((s[i] == 'D') or s[i] == 'M' and prev == 'C'):
            sum += (romanDict[s[i]] - 200)
            prev = ''
            continue
        sum += romanDict[s[i]]

    print('this is sum',sum)
    return sum
romanToInt("MCMXCIV")
