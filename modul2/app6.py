#take text from input: any text
#change each letter:
input1 = input("Write a text: ")
result = ''
previous=''
for letter in input1:
    if previous=='':
        previous=letter
        result=result + letter
    else:
        l=chr(ord(letter)+ord(previous))
        result = result + l
        previous=letter
print(result)