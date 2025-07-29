# Write a program for the 8 puzzle problem by taking the following initial and final states
import copy

def up(matrix,curr):
    x,y = curr
    if x > 0:
        new_matrix = copy.deepcopy(matrix)
        new_matrix[x][y],new_matrix[x-1][y] = new_matrix[x-1][y],new_matrix[x][y]
        return new_matrix
    return None

def left(matrix,curr):
    x,y = curr
    if y > 0:
        new_matrix = copy.deepcopy(matrix)
        new_matrix[x][y],new_matrix[x][y-1] = new_matrix[x][y-1],new_matrix[x][y]
        return new_matrix
    return None

def down(matrix,curr):
    x,y = curr
    if x < len(matrix)-1:
        new_matrix = copy.deepcopy(matrix)
        new_matrix[x][y],new_matrix[x+1][y] = new_matrix[x+1][y],new_matrix[x][y]
        return new_matrix
    return None

def right(matrix,curr):
    x,y = curr
    if y < len(matrix[0])-1:
        new_matrix = copy.deepcopy(matrix)
        new_matrix[x][y],new_matrix[x][y+1] = new_matrix[x][y+1],new_matrix[x][y]
        return new_matrix
    return None

def is_same_states(s,g):
    return s==g

def find_pos(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]==0:
                return [i,j]

def solve(initial,final):
    if(is_same_states(initial,final)):
        return True

    visit=[]
    q=[]
    visit.append(initial)
    q.append(initial)

    while(q):
        current=q.pop(0)
        curr=find_pos(current)

        child=[up(current,curr),down(current,curr),right(current,curr),left(current,curr)]

        for state in child:
            if state and not any(is_same_states(prev,state) for prev in visit):
                if is_same_states(state,final):
                    return True
                visit.append(state)
                q.append(state)
    return False
    

initial=[[1,2,3],[8,0,4],[7,6,5]]
initial1=[[1,2,3],[8,0,4],[7,6,5]]
final=[[2,8,1],[0,4,3],[7,6,5]]
print(solve(initial,final))

# print(solve(initial,initial1))