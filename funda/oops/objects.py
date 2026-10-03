# This class represents a car with a model name and its price.
class Car:
    # Initialize the car with its model and price.
    def __init__(self, model, price):
        self.model = model
        self.price = price

    # Display the current model of the car.
    def show_model(self):
        # Print a readable message using the car's model.
        print(self.model + " is a car model")

    # Update the car model with a new value.
    def update_model(self, newmodel):
        self.model = newmodel

# Create a Car object with an initial model and price.
car = Car("Go", 1000000)
# Show the current model before updating it.
car.show_model()
# Change the model name to a new value.
car.update_model("Alto")
# Show the new model after the update.
car.show_model()



class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade     # constructor initialising data

stu1 = Student("Rohit", "first")   # stu1 object holds its own data
stu2 = Student("Gru","fifth")      # stu2 object holds its own data

print(stu1.name+ " Grade: "+stu1.grade)  
print(stu2.name+ " Grade: "+stu1.grade)  
