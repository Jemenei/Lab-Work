#ex 1
def multiply_list(list):
    result = 1
    for x in list:
        result = result * x
    return result

list = [1, 2, 3, 4, 5, 6]
print(multiply_list(list))



#ex 2
def count_upper_lower(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower:
            lower_count += 1
    return upper_count, lower_count


def main():
    user_input = input()
    upper_count, lower_count = count_upper_lower(user_input)
    print("Number of uppercase letters:", upper_count)
    print("Number of lowercase letters:", lower_count)

if __name__ == "__main__":
    main()



#ex 3
def is_palindrom(string):
    clean_string = string.lower().replace(" " , "")
    return clean_string == clean_string[::-1]

def main():
    string_input = input()
    if is_palindrom(string_input):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()



#ex 4
import math, time

def calculate_squareroot(num, ml):
    time.sleep(ml / 1000)
    result = math.sqrt(num)
    return result

def main():
    num = int(input())
    ml = int(input())
    result = calculate_squareroot(num, ml)
    print(f"Square root of {num} after {ml} milliseconds if {result}")

if __name__ == "__main__":
    main()



#ex 5
def all_true(t):
    return all(t)

def main():
    tuple = (True, True, True)
    print(all_true(tuple))

if __name__ == "__main__":
    main()
