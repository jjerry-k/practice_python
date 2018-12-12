a = 16
b = 16.0
c = '16'
d = True

print("Type of a : ", type(a), a) # Type of a :  <class 'int'> 16
print("Type of b : ", type(b), b) # Type of b :  <class 'float'> 16.0
print("Type of c : ", type(c), c) # Type of c :  <class 'str'> 16
print("Type of d : ", type(d), d) # Type of d :  <class 'bool'> True

print("Type of float(a) : ", type(float(a)), float(a)) # Type of float(a) :  <class 'float'> 16.0
print("Type of int(b) : ", type(int(b)), int(b))       # Type of int(b) :  <class 'int'> 16
print("Type of int(c) : ", type(int(c)), int(c))       # Type of int(c) :  <class 'int'> 16
print("Type of float(c) : ", type(float(c)), float(c)) # Type of float(c) :  <class 'float'> 16.0
print("Type of int(d) : ", type(int(d)), int(d))       # Type of int(d) :  <class 'int'> 1
print("Type of float(d) : ", type(float(d)), float(d)) # Type of float(d) :  <class 'float'> 1.0