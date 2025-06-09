# Write a Python program to implement Travelling Salesman Problem (TSP). Take the starting node from the user at run time. 
graph=[[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
no_of_cities=len(graph) 
best_path=[]
min_cost=float('inf')


def tsp(scity,curr_city,path,visited,cost):
    global min_cost,best_path
        
    if len(path)==no_of_cities:
        tcost=cost+graph[curr_city][scity]
        if tcost<min_cost:
           min_cost=tcost
           best_path=path[:]+[scity+1]
        return

    for next_city in range(no_of_cities):
        if next_city not in visited:
            path.append(next_city+1)
            visited.append(next_city)
            tsp(scity,next_city,path,visited,cost+graph[curr_city][next_city])
            visited.pop()
            path.pop()

node=int(input("Enter The Starting Node: "))
tsp(node-1,node-1,[node],[node-1],0)
print(best_path)
print(min_cost)