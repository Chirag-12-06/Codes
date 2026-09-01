# Given two jugs- a 4 liter and 3 liter capacity. Neither has any measurable markers on it. 
# There is a pump which can be used to fill the jugs with water.
# Simulate the procedure in Python to get exactly 2 liter of water into 4-liter jug
visited = []
jug1=4
jug2=3
target=2

def Water(amt1,amt2):
    if(amt1 == target and amt2 == 0) or (amt2 == target and amt1 == 0):
        print(amt1,amt2)
        return True

    if (amt1,amt2) in visited:
        return False

    visited.append((amt1,amt2))
    print(amt1,amt2)

    return (Water(amt1,0) or
           Water(0,amt2) or
           Water(jug1,amt2) or
           Water(amt1,jug2) or
           Water(amt1 - min(amt1,jug2-amt2),amt2 + min(amt1,jug2-amt2)) or
           Water(amt1 + min(amt2,jug1-amt1),amt2 - min(amt2,jug1-amt1)))

Water(0,0)