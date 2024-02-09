#ex 1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces


#ex 2
def Fahrenheit_to_Celsius(Fahrenheit):
    Celsius = (5 / 9) * (Fahrenheit - 32)
    return Celsius


#ex 3
def solve(numheads, numlegs):
    rabitts = (numlegs - 2 * numheads) // 2
    chikens = numheads - rabitts

    if numheads >= 0 and numlegs >= 0 and chikens * 2 and rabitts * 4 == numlegs:
        return chikens, rabitts
    else:
        print("Zhauap Zhok")

#Example
num_heads = 35
num_legs = 94
print(solve(num_heads, num_legs))
    

#ex 4
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def filter_prime(n):
    return [num for num in numbers if is_prime(num)]

#Example
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(filter_prime(numbers))


#ex 5
import itertools

def print_permutations():
    input = input("Enter a string: ")
    permutations  = itertools.permutations(input)

    for perm in permutations:
        print("".join(perm))

print_permutations()


#ex 6
def rev_words(sent):
    words = sent.split()
    reversed_words = words[::-1]

    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence

input_sent = input("Enter a sentence: ")

print("Reversed sentence: ", rev_words(input_sent))


#ex 7
def has_33(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] == 3 and numbers[i + 1] == 3:
            return True
    return False

#example ex. 7
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))


#ex 8
def spy_game(nums):
    count_0 = 0
    for i in nums:
        if i == 0:
            count_0 += 1
        elif i == 7 and count_0 >= 2:
            return True
    return False

#example ex. 8
print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))


#ex 9
import math
def volume_sphere(R):
    volume  = (4 / 3) * math.pi * (R ** 3)
    return volume

#example ex. 9
print(volume_sphere(4))


#ex 10
def unique_list(l):
    x = []
    for i in x:
        if i not in x:
            x.append(i)
    return x

#example ex.10
print(unique_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(unique_list([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))
print(unique_list([1, 2, 2, 2, 3, 4, 5]))


#ex 11
def is_polindrom(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]

word = input("Enter a word:")
if is_polindrom(word):
    print(f"{word} is a palindrom")
else:
    print(f"{word} is not a palindrom")


#ex 12
def histogram(numbers):
    for num in numbers:
        print('*' * num)
    
#example ex.12
histogram[4, 9, 7]


#ex 13
import random

def guess_the_number():
    secret_number = random.randint(1, 20)
    guess_taken = 0

    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20")

    while True:
        print("take a guess.")
        guess = int(input())

        guess_taken += 1

        if guess < secret_number:
            print("Your guess if too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            break

    print(f"Good job, {name}! You guessed my number in {guess_taken} guesses!")

guess_the_number()
