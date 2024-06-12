def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    oriNum = x
    newNum = ''
    if (x<0):
        return False
    if (x<9):
        return True
    while(x>0):
        num = x%10
        newNum += str(num)
        x = x//10


    if(int(newNum) == oriNum):
        return True

    return False

print(isPalindrome(121))
