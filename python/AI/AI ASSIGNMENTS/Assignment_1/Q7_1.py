# i) Write a function which takes principal amount, interest rate and time. This function returns compound interest.

def Compound(p,r,t):
    amt = p*((1+r)**t)
    return amt-p

def main():
    p= float(input("Enter the Principal: "))
    r= float(input("Enter the Intrest Rate: "))
    t= int(input("Enter the Time: "))

    print("Compound Intrest:",Compound(p,r,t))

main()
