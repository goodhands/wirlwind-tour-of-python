# set the midpoint        
midpoint = 5
# make two empty lists        
lower = []; upper = []
# split the numbers into lower and upper        
for i in range(10):            
    if (i < midpoint):                
        lower.append(i)            
    else:                
        upper.append(i)
    
print("lower:", lower)        
print("upper:", upper)

# to continue operation on the next line use 
x = 1 + 2 + 3 + 4 + \       
    5 + 6 + 7 + 8 

# you can continue on the next line when items are inside parenthesis with a (\)
x = (1 + 3 + 5 + 6 +
4 + 7 + 7)

# python doesn't require a semicolon at the end of a statement but optionally you could use a semi colon to put 2 statements on a line:
list = []; jar = []

#Indentation matters!!!

#Parenthesis; for grouping or initiating methods
L = [1,2,3,4]
L.sort() #initiating

w = 2 + (4-5)

#Variables are pointers! And not buckets unlike PHP or C
x = 1         # x is an integer        
x = 'hello'   # now x is a string        
x = [1, 2, 3] # now x is a list 

#If we have two variable names pointing to the same `mutable` object, then changing one will change the other as well
x = [1, 2, 3]        
y = x #assigning y to the value of x
print(y)
x.append(4) # append 4 to the list pointed to by x        
print(y) # y's list is modified as well!

# Strings, numbers and other simple styles are immutable; you can't change their value
x = 10        
y = x        
x += 5  # add 5 to x's value, and assign it to x        
print("x =", x)        
print("y =", y)
# Output:
# x = 15 y = 10 

# There are types in Python, they are just not attached to the variables (pointer) but the objects being pointed to
x = 4         
type(x)
# int
x = 'hello'         
type(x)
# str
x = 3.14159         
type(x)
# float

# Making  number checks with comparison operators
#25 is odd          
25 % 2 == 1

# check if a is between 15 and 30          
a = 25          
15 < a < 30

#XOR
x=4
(x > 1) != (x < 10)

#OR
(x > 10) or (x % 2 == 0)

#NOT
not (x < 6)

#AND
(x < 6) and (x > 2)

#Identity operators: is and is not
a = [1,2,3]
b = [1,2,3]

a is b #false; because a and b are not identical objects. they have the same data type but do not point to the same object.
a is not b #true

a = [1, 2, 3]          
b = a          
a is b  #true

#######################
# PYTHON IS SO COOOL! #
#######################

#Membership Operator; checks for membership within compound objects. Just like PHP in_array
1 in [1, 2, 3] #true

2 not in [1, 2, 3] #false

#-------------------------
#--Simple Types in Python--
#-------------------------
# int x = 1 Integers (i.e., whole numbers) 
# float x = 1.0 Floating-point numbers (i.e., real numbers) 
# complex x = 1 + 2j Complex numbers (i.e., numbers with a real and imaginary part) 
# bool x = True Boolean: True/False values 
# str x = 'abc' String: characters or text 
# NoneType x = None Special object indicating nulls

#Python Integers do not overflow and they do division upcasts to floating point type in Python 3:
5 / 2 # 2.5 
#Remember, the floor division operator (//) returns the outcome of a division and throws aaway any remainder or decimal
5 // 2 #2

#Floating-Point Numbers 
# The floating-point type can store fractional numbers. 
# They can be defined either in standard decimal notation, or in exponential notation:
x = 0.000005        
y = 5e-6 #equivalent of 5 x 10-6 (e = 10 times the number on the LHS)
print(x == y) # True

#Type casting an int to float
float(1) #1.0
