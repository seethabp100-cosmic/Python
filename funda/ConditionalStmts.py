#the if statement runs a block of code when a condition is True. If the condition is False, the else block runs. 
# This helps programs make decisions based on conditions.

#1 if block
a = 2
b = 1
if(a > b):
    print("a>b: ",a>b);


#2 if else block
a = "raju"
b = ["yellow","red","black"]
if("yellow" in b):
    print(a," where yellow shirt todat")
else:
    print(a," where normal shirt")


#3 if elif
a = [1,2,3,4]
b = 2
c =3
d =4
e =12
if(b in a):
    print("a contains: ",b)
elif(c in a):
    print("a contains: ",c)
elif(d in a):
    print("a contains: ",d)
else:
    print("a doesnt contain: ",e)



#loops: iterate a sequence and execute blocks, execute a block until condition goes false
#1 for loop : iterate list, list of dictionarys, string, seq of numbers

a = [1,2,3,4,5]
for i in a:
    print(i)

list1 = ["list", "dictionary", "tuple"]
for i in list1:
    print(i)

#2 while
count = 0
while count < 3:
    count+=1
    print("count: ",count)