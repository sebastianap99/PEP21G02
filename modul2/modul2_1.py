name='Sebastian'
age=22
print("name: ",name,", age: :",age)

#type function

result=type(name)
print(result)
result=type(age)
print(result)

print(type(name*5))

print(id(name))

print(8+8)
print((8).__add__(8))
print(8*"text")

print((8).__mul__("text"))
print(("text").__mul__(8))

print(8-8)
print((8).__sub__(8))

print(8/8)
print((8).__truediv__(8))

#float
print(type((8).__truediv__(8)))

print(8**8)
print((8).__pow__(8))
print(pow(8,8))

a=3
b=4
c=5
x = (-b + ((b**2) - 4 * a * c)**(1/2))/(2*a)
print(x)
x = (-b - ((b**2) - 4 * a * c)**(1/2))/(2*a)
print(x)

bsqr= b.__pow__(2)
multi= (4).__mul__(a.__mul__(c))
dif= bsqr.__sub__(multi)
dif=float(dif)
var=(1).__truediv__(2)
rad=dif.__pow__(var)
b= complex(b)
dif2=(-b).__sub__(rad)
mul1=(2).__mul__(a)
ec= dif2.__truediv__(mul1)
print(ec)

#Complex
nr1=1.0+1.0j
print(type(nr1))
nr2=3+5j
print(nr1+nr2)

#string
my_str1="My String"
print(my_str1)
my_str="My String"


phone="0747.655.444"
split2=phone.split()

print(True+True)

