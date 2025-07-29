# 2 Write a Program to input basic salary of an employee and calculate its Gross salary according to following: 
# Basic Salary <= 10000 : HRA = 20%, DA = 80% Basic Salary <= 20000 
# : HRA = 25%, DA = 90% Basic Salary > 20000 : HRA = 30%, DA = 95%. 

sal = int(input("Enter your Salary: "))

if(sal<=10000):
    hra=0.2
    da=0.8
elif(sal<=20000):
    hra=0.25
    da=0.9
else:
    hra=0.3
    da=0.95
print("Your Gross Salary:",sal*(1+hra+da))