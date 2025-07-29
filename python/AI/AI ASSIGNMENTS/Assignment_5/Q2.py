import copy

Items={'A':{'Name':"Mirror",'Weight':2,'Value':3},
       'B':{'Name':"Silver Nugget",'Weight':3,'Value':5},
       'C':{'Name':"Painting",'Weight':4,'Value':7},
       'D':{'Name':"Vase",'Weight':5,'Value':9}
       }

Times=4
Capacity=9
Mutate_Order=[2,0,3,1]
Mutate=0

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
    global Mutate_Order,Mutate
    
    c[Mutate_Order[Mutate]] = 1-c[Mutate_Order[Mutate]]
    Mutate+=1
    if (Mutate>3):
        Mutate = 0
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
    global Times,Capacity   
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
             if(new_pop[i][1]<=Capacity and not any (new_pop[i]==com for com in mod_pop)):
                    mod_pop.append(new_pop[i])
                    j+=1
             i+=1
                     
       print(mod_pop)
       print('\n')
       Times-=1
    mod_pop.sort()
    print('Items:')
    for i in range(len(mod_pop[-1][2])):
           if(mod_pop[-1][2][i]==1):
              print(Items[chr(i+65)]['Name']) 
    print('\n',end='')
    print('Total Value:',mod_pop[-1][0],'$') 
    print('Total Weight:',mod_pop[-1][1],'Kg') 
    
                  
    
def main():
       modified_pop = []
       for chrm in population:
              ans = three_tuple(chrm)
              modified_pop.append(ans)
       genetic(modified_pop)

main()


 
# chromosome followed by single bit mutation of first offspring (produced through crossover). 
# Bit chosen for mutation follows this cyclic order {XC,XA,XD,XB} 