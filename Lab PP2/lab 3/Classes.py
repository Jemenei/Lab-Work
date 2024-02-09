#ex 1:
class String:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print(self.input_string.upper())

    
user = String()
user.getString()
user.printString()



#ex 2:
class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0
    

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2



#ex 3
class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width



#ex 4
import math

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        
    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    


#ex 5
class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance  = balance

    def deposit(self, summa):
        if summa > 0:
            if summa <= self.balance:
                self.balance += summa
                print(f"Withdrawn: {summa}.\nNew balance: {self.balance}")
            else:
                print("Not enough funds")
        else:
            print("Wrong withdrawal amount")
            
#Account class
acc = Account("Suleimen Madi", 1000)

#Test
print(f"Balance: {acc.balance}")
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(1500)
print(f"Final Balance: {acc.balance}")



#ex 6
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = [2, 3, 4, 5, 6, 7, 8, 9, 10]

prime_numbers = list(filter(lambda x: is_prime(x), num))

print("Prime numbers:", prime_numbers)