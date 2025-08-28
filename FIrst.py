print("Hello World")
x,y,z=5,6,7
print(id(x))
print(id(y))
print(id(z))

#unpack a collection(in list,tuple)
f=["a","b","c"]
x,y,z=f
print(x)
print(y)
print(z)

#globalvariable

def myfunc():
    global x
    x="awesome"

myfunc()
print("Python is " +x)