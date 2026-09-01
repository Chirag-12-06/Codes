# A) Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of information,
# A method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. 
# Print the two attributes individually, and then call both methods. 
class Restaurant:
    def __init__(self,res,cus):
        self.restaurant_name=res
        self.cuisine_type=cus

    def describe_restaurant(self):
        print("Restaurant_name:",self.restaurant_name)
        print("Cuisine_type:",self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name,"is OPEN !!!!")



restaurant=Restaurant("dw","ef")
restaurant.describe_restaurant()     
restaurant.open_restaurant()
print()


# B) Make a class called User. Create two attributes called first_name and last_name, and create several other attributes that are typically stored in a user profile. 
# Make a method called describe_user() that prints a summary of the user’s information. 
# Make another method called greet_user() that prints a personalized greeting to the user. 
# Create several instances representing different users, and call both method for each user.
class User:
    def __init__(self,fname,lname,no,email,gender):
        self.first_name=fname
        self.last_name=lname
        self.no=no
        self.email=email
        self.gender=gender

    def describe_User(self):
        print("User_name:",self.first_name,self.last_name)
        print("Mobile No:",self.no)
        print("Email:",self.email)
        print("Gender:",self.gender,"\n")

    def greet_user(self):
        print("Hello,",self.first_name,self.last_name)



User1=User("Priya","Goel",34564527,"de@g.com","M")
User2=User("Mike","Tyson",3876364527,"op@gin.com","F")

User1.greet_user()
User1.describe_User()

User2.greet_user()
User2.describe_User()
