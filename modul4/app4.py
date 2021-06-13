def conversation():
    name=None
    age=None
    def hello():
        print('Hello John ')
    def respone_hello():
        nonlocal name
        name= input('My name is ')
    def question():
        print(name ,', how is the weather ?')
    def question2():
        print(name, ", how old are you?")
        nonlocal age
        age=input("My age is ")


    return hello , respone_hello , question, question2
c=conversation()
c[0]()
c[1]()
c[2]()
c[3]()
