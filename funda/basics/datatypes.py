print("hello world")  #start

#variable assignment, python contains no variabble declaration, directly assign to a value
# int, float, String
a = 23      #interger value
f = 12.12   #floating value
str = "Hello" #String
print(a,f,str,sep="-")  #printing the above declared variables, "sep" is default variable separator(by default space(" "), can be add "-","_")

#Datatypes: 
"""
Numeric: Integer, Floating values, Complex numbers
Boolean
Dicionary
Set
Sequence type: String, List, Tuple
""" 
print("Hello world");   #String datatype
print(123);  #number datatype(int)
print(123.00) #float
print(2>1);  #boolean
print([123,234,456]); #list
print((123,"abc","xyz", True)) # tuple
dict1 = {"name":"Doe","age":24} #dictionary
print(dict1)    
set1 = {"abc","acv","abc"}  #set(wont allow duplicate values)
print(set1)
x = b"abcs"
print(x);


#python i/o: Python provide predefined/built-in function to take input from user and display/print on screen
x = input("Enter a value: ");   #String
print(x);

#to take input from user for integer, we need a function int()
x = int(input("Enter a int value: "));
print("int value:: ",x);

# type() function
x =int(input("Enter int: "));
print("int value: ",x, "datatype: ",type(x));

x =float(input("Enter int: "));
print("float value: ",x, "datatype: ",type(x));

x =bool(input("Enter int: "));
print("bool value: ",x, "datatype: ",type(x));

x =input("Enter int: ");
print("str value: ",x, "datatype: ",type(x));
# input() always return string, int(),float(),bool() converts input value into respective data type.

#print function examples
# to open txt file and read content
file = open("C:/Users/bhanu/bhanu/learning/Python/funda/assets/sample.txt", "r")
content = file.read();
print(content, sep="|")

#to print error stream instead of default o/p stream
import sys
company = "GFG"
loc = "Noida"
mail = "contact@gfg.org"
print(company, loc, mail, file=sys.stderr)