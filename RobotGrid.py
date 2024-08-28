class Solution:
    def lookForPath(matrix):
        currCoor = [0,0]
        deadEndSpots = []
        while(True):
                if(currCoor[0] == len(matrix)-1 and currCoor[1] == len(matrix[0])-1):
                    return True
                if(currCoor in deadEndSpots):
                     return False
                if(matrix[currCoor[0]][currCoor[1]+1]):
                     currCoor[1] += 1
                elif(matrix[currCoor[0]+1][currCoor[1]]):
                     currCoor[0] += 1
                else:
                     deadEndSpots.append(currCoor)

        return False
