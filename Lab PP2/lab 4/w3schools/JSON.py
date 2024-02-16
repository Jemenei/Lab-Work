#Examples in w3schools



#ex 1
import json



#ex 2
import json

x = '{"name" : "John", "age" : 30, "city" : "New York"}'

y = json.loads(x)

print(y["age"])



#ex 3
import json

x = {
    "name"  : "Madi",
    "age" : 18,
    "city" : "Aktau 7292"
}

y = json.dumps(x)
print(y)



#ex 4
import json

print(json.dumps({"name" : "Madi", "age" : 18}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))



#ex 5
import json

x = {
    "name" : "Madi",
    "age" : 18,
    "Married" : False,
    "Divorced" : False,
    "Sisters/Brothers" : ("Amina", "Gulfairyz", "Toqzhan", "Dariya"),
    "Pets" : None,
    "Cars" : [
        {"model" : "Lx 570"},
        {"model" : "Toyota Camry 70"}
    ]
}

print(json.dumps(x))



#ex 6
json.dumps(x, indent=4)



#ex 7
json.dumps(x, indent = 4, separators=(". ", " = "))



#ex 8
json.dumps(x, indent=4, sort_keys=True)
