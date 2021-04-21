"""
Take text from input: any text
change each letter
"""
from random import randrange

x=input("input any text: ")
for letter in x:
    print(chr(ord(letter)+randrange(10)), end="")