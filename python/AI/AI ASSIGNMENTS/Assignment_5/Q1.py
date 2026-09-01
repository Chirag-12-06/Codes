import copy

Items={'A':{'Weight':45,'Value':3},
       'B':{'Weight':40,'Value':5},
       'C':{'Weight':50,'Value':8},
       'D':{'Weight':90,'Value':10}
       }

Times=10
Capacity=100
Mutate=3

population=[[1,1,1,1],
            [1,0,0,0],
            [1,0,1,0],
            [1,0,0,1]]

def three_tuple(ch):
    wt,val=0,0
    for i in range (len(ch)):
        if ch[i] == 1:
            wt += Items[(chr)(i+65)]['Weight']
            val += Items[(chr)(i+65)]['Value']
    thr_tpl = [val,wt,ch]
    return thr_tpl

def mutation(c):
    global Mutate
    
    c[Mutate] = 1-c[Mutate]
    Mutate = Mutate - 1
    if (Mutate < 0):
        Mutate = 3
    return(c)

def crossover(p1,p2):
    mid = len(p1)//2
    c1 = copy.deepcopy(p1)
    c2 = copy.deepcopy(p2)

    for i in range(mid,len(p1)):
        c1[i] = p2[i]
        c2[i] = p1[i]
    return[c1,c2]
    
def genetic(mod_pop):
    global Times   
    while(Times):
       mod_pop.sort()
       print(mod_pop)
       p1 = mod_pop[-1][-1]
       del mod_pop[-1]
       p2 = mod_pop[-1][-1]
       del mod_pop[-1]
       print(mod_pop)
       children = crossover(p1,p2)
       c1 = children[0]
       c2 = children[1]
       c1 = mutation(c1)

       new_pop=[three_tuple(p1),three_tuple(p2),three_tuple(c1),three_tuple(c2)]
       new_pop.sort(reverse=True)
       print(new_pop)
       i,j=0,0
       while(i<len(new_pop) and j<2):
             if(new_pop[i][1]<=100 and not any (new_pop[i]==com for com in mod_pop)):
                    mod_pop.append(new_pop[i])
                    j+=1
             i+=1
                     
       print(mod_pop)
       print('\n')
       Times-=1
    mod_pop.sort()   
    print('Total Value:',mod_pop[-1][0]) 
    print('Total Weight:',mod_pop[-1][1]) 
    print('Items:',end=' ')
    for i in range(len(mod_pop[-1][2])):
           if(mod_pop[-1][2][i]==1):
              print(chr(i+65),end=' ') 
                  
    
def main():
       modified_pop = []
       for chrm in population:
              ans = three_tuple(chrm)
              modified_pop.append(ans)
       genetic(modified_pop)

main()
