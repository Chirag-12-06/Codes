class Student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        return sum/3
    
    @staticmethod
    def hello():
        print("hello")

s1=Student("vfe",[34,76,43])
print(s1.avg())
s1.hello()