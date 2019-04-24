<<<<<<< HEAD
#Python Funadamentals
#Uncomment particular block to run

#Print
'''
print("Hello World")
'''

#Arithmetic
'''
a=1
b=2
c=a+b
print("c is {}".format(c) )
print("c is",c,"that's it" )
print("c is %d" % (c) )
'''

#Conditional Statements
'''
a=2
b=2
if a>b:
	print("a>b")
elif a==b:
	print("b=a")
else:
	print("b>a")

x="less" if a<2 else x="more"  #Ternary if-else
print("x is {}".format(x))
'''

#Loops
'''
for x in range(2, 30, 3):
  print(x)   
for x in "samplestring":
  print(x)
'''

#Objects and classes
'''
class Book:
	def __init__(self,author,price):
		self.author=author
		self.price=price
	def printDetails(self):
		print("author: " + self.author)
		print("price: {} ".format(self.price))	

b1 = Book('Pyhton Programming',120)
b2 = Book('C++ Programming',150)
#b1.printDetails()

class Person:
	def __init__(self,name,age):
    	self.name=name
		self.age=age
	def printAll(self):
		print("Name: " + self.name)
		print("age: {}".format(self.age))

p1=Person("John",34)
p2=Person("Jane",29)
#p1.printAll()

p1.bookOwned=b1 #New Dynammically created attribute
p1.bookOwned.printDetails()
'''

#List
'''
l=list()
l=[2,3,6,8]  
l.append(9)    #To add elements use append()
l2=[item for item in list if item%3==0] #List Comprehension
print(l2)      #preserves order
'''

#Sets
'''
s=set()
s.add(1)  #To add elemets use add()
print(s)  #doesn't preserve order

squaredSet={x**2 for x in [1,2,2,3,3,3,4,4,4,4]} #Set Comprehension
'''

#Dictionary
'''
d={} #or d=dict()
d["square"]=2
d["cube"]=3
d["10"]=100

for key,value in d.items():
	print("Key: {}, Value: {}".format(key,value))

dict1={'a':25,'b':30,'A':7}         #Dictionary Comprehension
print({k.lower():dict1.get(k.lower(),0)+dict1.get(k.upper(),0) for k in dict1.keys() })  #Add values at same characters in upper case and lower case. 
=======
#Python Funadamentals
#Uncomment particular block to run

#Print
'''
print("Hello World")

a=1
b=2
c=a+b
print("c is {}".format(c) )
print("c is",c,"that's it" )
print("c is %d" % (c) )
'''

#Conditional Statements
'''
a=2
b=2
if a>b:
	print("a>b")
elif a==b:
	print("b=a")
else:
	print("b>a")

x="less" if a<2 else x="more"  #Ternary if-else
print("x is {}".format(x))
'''

#Loops
'''
for x in range(2, 30, 3):
  print(x)   
for x in "samplestring":
  print(x)
'''

#Objects and classes
'''
class Book:
	def __init__(self,author,price):
		self.author=author
		self.price=price
	def printDetails(self):
		print("author: " + self.author)
		print("price: {} ".format(self.price))	

b1 = Book('Pyhton Programming',120)
b2 = Book('C++ Programming',150)
#b1.printDetails()

class Person:
	def __init__(self,name,age):
    	self.name=name
		self.age=age
	def printAll(self):
		print("Name: " + self.name)
		print("age: {}".format(self.age))

p1=Person("John",34)
p2=Person("Jane",29)
#p1.printAll()

p1.bookOwned=b1 #New Dynammically created attribute
p1.bookOwned.printDetails()
'''

#List
'''
l=list()
l=[2,3,6,8]  
l.append(9)    #To add elements use append()
l2=[item for item in list if item%3==0] #List Comprehension
print(l2)      #preserves order
'''

#Sets
'''
s=set()
s.add(1)  #To add elemets use add()
print(s)  #doesn't preserve order

squaredSet={x**2 for x in [1,2,2,3,3,3,4,4,4,4]} #Set Comprehension
'''

#Dictionary
'''
d={} #or d=dict()
d["square"]=2
d["cube"]=3
d["10"]=100

for key,value in d.items():
	print("Key: {}, Value: {}".format(key,value))

dict1={'a':25,'b':30,'A':7}         #Dictionary Comprehension
print({k.lower():dict1.get(k.lower(),0)+dict1.get(k.upper(),0) for k in dict1.keys() })  #Add values at same characters in upper case and lower case. 
>>>>>>> d9174b9fcd5ffba207cc2e560d720eb917727710
