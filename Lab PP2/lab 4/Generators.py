#ex 1
n = int(input())

def squares(n):
    for i in range(n):
        yield i ** 2

for x in squares(n):
    print(x)



#ex 2
n = int(input())

def even_numbers(n):
    for i in range(n):
        if i % 2 == 1:
            yield i
    
for x in even_numbers(n):
    print(x)



#ex 3
n = int(input())

def divisible(n):
    for i in range(n+1):
        if (i % 3 == 0) and (i % 4 == 0):
            yield i
        
for x in divisible(n):
    print(x)




#ex 4
a, b = map(int, input().split())

def range_of_squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
for x in range_of_squares(a, b):
    print(x)



#ex 5
n = int(input())

def reversse_list(n):
    for i in range(n, -1, -1):
        yield i

for x in reversse_list(n):
    print(x)
