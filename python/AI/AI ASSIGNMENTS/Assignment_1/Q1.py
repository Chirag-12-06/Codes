# A class with 10 students wants to produce some information from the results of the four standard tests in Maths, Science, English and IT. 
# Each test is out of 100 marks. 
# The information output should be the highest, lowest and average mark for each test and the highest, lowest and average mark overall.
import statistics
marks={
    'Maths': [75, 98, 92, 69, 70, 77, 81, 95, 73, 89],
    'Science': [70, 91, 89, 50, 83, 79, 98, 93, 50, 74],
    'English': [80, 87, 78, 70, 82, 90, 76, 84, 79, 75],
    'IT': [90, 70, 87, 83, 92, 98, 89, 94, 80, 78]
}

high=[]
low=[]
avg=[]

for i in marks:
    print("For",i)
    h=max(marks[i])
    print("Highest" ,h)
    high.append(h)
    l=min(marks[i])
    print("Lowest" ,l)
    low.append(l)
    a=statistics.mean(marks[i])
    print("Average" ,a)
    avg.append(a)
    print()


print("Overall Statistics")
print("Highest" ,max(high))
print("Lowest" ,min(low))
print("Average",statistics.mean(avg))