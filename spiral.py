import numpy as np #то что надо
import math
def spiral(string):
    try:
        
        l = len(string)
        sl = int(math.ceil(np.sqrt(l)))
        matrix = [[' ' for i in range(sl)] for i in range(sl)]
        s = 1
        li = list(string)
        x = 0
        y = 0
        if sl % 2 == 1:
            x, y = math.floor(sl/2), math.floor(sl/2)

        else:
            x, y = int(sl/2), int((sl/2)-1)
            
            
        matrix[x][y] = li[0]

        li.pop(0)
        d = 0
        
        for i in range (l):
            if d == 0:
                for j in range(s):
                    y+=1
                    matrix[x][y] = li[0]
                    li.pop(0)
                d = 1
                continue
            elif d == 1:
                for j in range(s):
                    x+= -1
                    matrix[x][y] = li[0]
                    li.pop(0)
                d = 2
                s+=1
                continue
            elif d==2:
                for j in range(s):
                    y += -1
                    matrix[x][y] = li[0]
                    li.pop(0)
                d = 3
                continue
            else:
                for j in range(s):
                    x += 1
                    matrix[x][y] = li[0]
                    li.pop(0)
                d = 0
                s += 1
                continue
        
        for row in matrix:
            print(' '.join(list(map(str, row))))
    except:
        for row in matrix:
            print(' '.join(list(map(str, row))))
    return 0
string = input("Input string: ")            
spiral(string)
        
        
    