#1.1(page90)
def uniqueString(str):
    for i in range(len(str)):
        for j in range(i+1,len(str)):
            if(str[j] == str[i]):
                return False

    return True

print(uniqueString('abcde'))
print(uniqueString('abcaefa'))
print(uniqueString('a'))
