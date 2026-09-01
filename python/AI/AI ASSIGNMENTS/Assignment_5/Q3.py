import copy
import math
import random
T=500
open=[]
closed=[]


def F(s):
    return [(not(s[0]) or s[3]),(not(s[2]) or not(s[1])),(not(s[2]) or not(s[3])),(not(s[3]) or not(s[1])),(not(s[0]) or not(s[3]))]

def H(s):
    sum=0
    for i in F(s):
        sum+=i
    return sum

def moves(s):
    childs=[]
    for i in range(len(s)):
        si=copy.deepcopy(s)
        s[i]=1-s[i]
            
        if (si not in closed):
            childs.append([H(si),si])
    return childs


def S_A(s):
    global T
    if(H(s)==5):
        print("SOLUTION IS FOR VALUES",s)
        return
    open.append([H(s),s])
    closed.append(s)
    while (T):
        s=open[0]
        open.pop(0)
        if(s[0]==5):
            print("SOLUTION IS FOR VALUES",s)
            return
        ch=moves(s[1])
        for c in ch:
            print(c)
            delta_E=c[0]-s[0]
            P=1/(1+math.exp(delta_E/T))
            if P>random.random():
                open.append(c)
            closed.append(c)
        T-=5



def main():
    s=[1,1,1,1]
    c=S_A(s)
    
main()


# (Assume the following 3 random numbers:0.655,0.254.0.432) 
# Accept every good move and accept a bad move if probability is greater than 50%