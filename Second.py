var1=1 
var2= True
var3=10.023
var4=10+3j
print(type(var1)) #class 'int'
print(type(var2)) #class 'bool'
print(type(var3)) #class 'float'
print(type(var4)) #class 'complex'

#string line string(" " and ' ')
a="Hello World!"
print(a)
b='Hello My Friend!'
print(b)

#Multiline string('''  '''')
c='''Hi! nice to meet you'''
print(c)


#String Length
arr="AyushSinha"
print(len(arr))

#Check String
txt="The best things in life are free!"
print("free" in txt)

#Slicing Strings
b="Hello,World!" 
print(b[2:5])
c="Hello,World!" #From Start
print(b[:5])
b="Hello,World!" #TO The End
print(b[2:])
b="Hello,World!" #Negative 
print(b[-5:-2])

#Modify Strings
a="Hello,World!"
print(a.upper())
a="Hello,World!"
print(a.lower())
a="Hello,World!"
print(a.strip())