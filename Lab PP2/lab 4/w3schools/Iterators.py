#examples in w3schools:

#ex 1
mytuple = ("apples", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))



#ex 2
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))



#ex 3
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)



#ex 4
mystr = "banana"

for i in mystr:
    print(i)