#examples in w3schools



#ex 1
def myfunc():
    x = 300
    print(x)

myfunc()



#ex 2
def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()



#ex 3
x = 300

def myfunc():
    print(x)

myfunc()

print(x)



#ex 4
x = 300

def myfunc():
    x = 200
    print(x)

myfunc()

print(x)



#ex 5
def myfunc():
    global x
    x = 300

myfunc()

print(x)



#ex 6
x = 300

def myfunc():
    global x
    x = 200

myfunc()

print(x)