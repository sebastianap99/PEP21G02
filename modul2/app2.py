"""
Get from input abcdefg
Return bcdefgh

"""
x=input("Get input: ")

y1=ord(x[0:1])+1
z1=chr(y1)

y2=ord(x[1:2])+1
z2=chr(y2)

y3=ord(x[2:3])+1
z3=chr(y3)

y4=ord(x[3:4])+1
z4=chr(y4)

y5=ord(x[4:5])+1
z5=chr(y5)

y6=ord(x[5:6])+1
z6=chr(y6)

y7=ord(x[6:7])+1
z7=chr(y7)

print(z1,z2,z3,z4,z5,z6,z7,sep="")
