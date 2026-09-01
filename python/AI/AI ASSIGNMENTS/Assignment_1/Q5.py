# 5 D is a dictionary defined as D= {1:”One”, 2:”Two”, 3:”Three”, 4: “Four”, 5:”Five”}. 
D={
    1:"One",
    2:"Two",
    3:"Three",
    4:"Four",
    5:"Five"
    }


# (i) WAP to add new entry in D; key=6 and value is “Six” 
D[6]="Six"
print(D)


# (ii) WAP to remove key=2.
del(D[2])
print(D)


# (iii) WAP to check if 6 key is present in D.
if(6 in D):
    print("Present")
else:
    print("Not Present")


# (iv) WAP to count the number of elements present in D.
print(len(D))


# (v) WAP to add all the values present D.
print("".join(D.values()))