import copy

def compare(s,g):
    return s==g

def find_H(Matrix,Goal):
    count=0
    for i in range(len(Matrix)):
        for j in range(len(Matrix[0])):
            if Matrix[i][j]!=Goal[i][j]:
                count+=1
    return count

def pos(Matrix):
    for i in range(len(Matrix)):
        for j in range(len(Matrix[0])):
            if Matrix[i][j] ==0:
                return [i,j]

def up(matrix,position):
    x,y = position
    if x > 0:
        new_matrix = copy.deepcopy(matrix)
        new_matrix[x][y],new_matrix[x-1][y] = new_matrix[x-1][y],new_matrix[x][y]
        return new_matrix
    return None

def left(matrix,position):
    x,y = position
    if y > 0:
        new_matrix = copy.deepcopy(matrix)
        new_matrix[x][y],new_matrix[x][y-1] = new_matrix[x][y-1],new_matrix[x][y]
        return new_matrix
    return None

def down(matrix,position):
    x,y = position
    if x < len(matrix)-1:
        new_matrix = copy.deepcopy(matrix)
        new_matrix[x][y],new_matrix[x+1][y] = new_matrix[x+1][y],new_matrix[x][y]
        return new_matrix
    return None

def right(matrix,position):
    x,y = position
    if y < len(matrix[0])-1:
        new_matrix = copy.deepcopy(matrix)
        new_matrix[x][y],new_matrix[x][y+1] = new_matrix[x][y+1],new_matrix[x][y]
        return new_matrix
    return None

def best_first(s,goal):
    if compare(s,goal):
        return True

    open=[[find_H(s,goal),s]]
    closed=[]

    while (open):
        open.sort()
        curr=open[0]
        print(curr)
        open.pop(0)
        
        if compare(curr[1],goal):
            return True
        
        closed.append(curr[1])
        posi=pos(curr[1])

        dir=[up,down,left,right]
        
        for d in dir:
            child=d(curr[1],posi)
            if child and child not in closed and not any(compare(child,matrix[1])for matrix in open):
                open.append([find_H(child,goal),child])
            
    return False

   
initial=[[1,2,3],[8,0,4],[7,6,5]]
final =[[2,0,3],[1,8,4],[7,6,5]]
print(best_first(initial,final))

