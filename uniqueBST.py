def numTrees(n):
    """
    :type n: int
    :rtype: int
    """
    count = 0
    curr = 2
    for i in range(1,n+1):
        if(curr >n):
            break
        leftCount = 0
        rightCount = 0
        tempLeft = curr - 1
        tempRight = curr + 1

        while(tempLeft != i or tempRight <= n):
            if(tempLeft > i):
                leftCount += 1
            if(tempRight < n):
                rightCount += 1
            tempLeft -= 1
            tempRight += 1

        curr += 1
        count = (count + leftCount) if leftCount > rightCount else (count + rightCount)
    print(count)
    return count

numTrees(3)
