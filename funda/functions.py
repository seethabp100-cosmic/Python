#Functions: block of reusable code that performs a specific task
# pre-defined(built-in): print(), int(), len(), type()
# user defined: goes with keyword: def, and name it. 
"""
example: def add(a,b):
            <statements
            return expression
"""

def evenOdd(x):
    if(x%2==0):
        print("x is even")
    else:
        print("x is odd")
evenOdd(2)
evenOdd(10)
evenOdd(5)
evenOdd(15)


def addition(a,b):
    if(a>0 and b>0):
        print("add: ",a+b)

addition(10,20)

def substraction(a,b):
    if(a>0 and b>0):
        print("diff: ",a-b)

substraction(10,20)

def multiplication(a,b):
    if(a>0 and b>0):
            print("multiplication: ",a*b)

multiplication(100,5);

def division(a,b):
    if(a>0 and b>0):
            print("division: ",a/b)

division(100,5);

#2 pass statement in python
x = 10

if x > 5:
    pass  # Placeholder for future logic
else:
    print("x is 5 or less")

#3 pass statement in loops
# pass statement does nothing when interpreter read the pass statement. 
for i in range(5):
    if i>2:
        pass   # 
    elif(i<5):
        print("i is less than 5")