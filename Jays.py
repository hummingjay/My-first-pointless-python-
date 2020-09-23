N= input("What is your name?")
print('Welcome '+N)
print('How are you?') 
print('Fine or not fine')
x=input("-->")
if x=="Fine" : 
 print("Good to know")
else:
 print("WHY?")
print("Next we will go through some random pointless steps")
J=5
A=7
print(J+A)
print("J"+"A")
x=input("x=")
print(x)
y=input("y=")
print(y)
print(x==y)
numbers=list(range(10))
print(numbers)
nums=list(range(5))
print(nums[4])
nums=list(range(5,8))
print(len(nums))
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
x = 35e3
y = 12E4
z = -87.7e100
J = 5j

print(type(x))
print(type(y))
print(type(z))
print(type(J))
class cat:
 def __init__(self,color,legs):
    self.color = color
    self.legs = legs
felix = cat("ginger",4)
rover = cat("dog-colored",4)
stumpy = cat("brown",3)
print(felix.color)
