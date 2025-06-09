# 6 WAP to create a list of 100 random numbers between 100 and 900. Count and print the:  
# (i) All odd numbers 
# (ii) All even numbers 
# (iii) All prime numbers

def is_prime(n):
    if(n==1):
        return False
    for i in range(2,n-1,1):
        if(not (n%i)):
            return False
    return True

import random
L=[random.randint(100,900) for i in range(100)]

even=[]
odd=[]
primes=[]

for i in L:
    if is_prime(i):
        primes.append(i)
    if i%2:
        odd.append(i)
    else:
        even.append(i)

print("For Odd")
print("Nos:",len(odd))
print("List:",odd,"\n")

print("For Even")
print("Nos:",len(even))
print("List:",even,"\n")

print("For Prime")
print("Nos:",len(primes))
print("List:",primes)

