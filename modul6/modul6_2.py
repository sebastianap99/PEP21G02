#open
file=open('my_file.txt','w')
print(type(file))
file.write('My new text file\n')
file.close()

with open('my_file.txt','a') as file:
    file.write('Random text file')