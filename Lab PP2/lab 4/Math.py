#ex 1
def deg_to_rad(degree):
	radian = degree * 0.0174533
	return radian

degree = int(input())
print(deg_to_rad(degree))



#ex 2
def area_of_trapezoid(height, first_value, second_value):
	area = ((first_value + second_value) / 2) * height
	return area

height, first_value, second_value = map(int, input().split())
print(area_of_trapezoid(height, first_value, second_value))



#ex 3
import math

def area_of_regular_polygon(n, length):
    area = (n * length ** 2) / (4 * math.tan(math.pi / n))
    return int(area)

n, length = map(int, input().split())
print(area_of_regular_polygon(n, length))



#ex 4
def area_of_parallelogram(length, height):
    area = length * height
    return area

length, height = map(int, input().split())
print(area_of_parallelogram(length, height))
