#Examples in w3schools



#ex 1 | RegEx Module
import re



#ex 2 | RegEx in Python
import re

txt  = "The rain in Spain"
x = re.search("^The.*Spain$", txt)



#Metacharacters
#ex 3
import re

txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m"

x = re.findall("[a-m]", txt)
print(x)



#ex 4
import re

txt = "That will be 59 dollars"

#Find all digit characters:

x = re.findall("\d", txt)
print(x)



#ex 5
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "0":

x = re.findall("he..o", txt)
print(x)



#ex 6
import re

txt = "hello planet"

#Check if the string starts with hello:
x = re.findall("^hello", txt)

if x:
    print("Yes, the string starts with 'hello'")
else:
    print("No match")



#ex 7
import re

txt = "hello planet"

#Check if the string ends with 'planet'
x = re.findall("planet$", txt)

if x:
    print("Yes, the string ends with 'planet'")
else:
    print("No match")



#ex 8
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or more (any) characters, and an "o"

x = re.findall("he.*o", txt)
print(x)



#ex 9
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by 1 or more (any) characters, and an "o"

x = re.findall("he.+o", txt)
print(x)



#ex 10
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or 1 (any) character, and an "0":

x = re.findall("he.?", txt)
print(x)

#This time we got no match, because there were not zero, not one, but two characters between "he" and  the "o"



#ex 11
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed exactly 2 (any) characters, and an "o":

x = re.findall("he.{2}o", txt)
print(x)



#ex 12
import re

txt = "The rain in Spain falls mainly in the plain!"

#Chech if the string contains either "falls" or "stays":

x = re.findall("falls|stays", txt)
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")



#Special Sequence
#ex 1
import re

txt = "The rain in Spain"

#Chech if the string starts with "The":

x = re.findall("\AThe", txt)
print(x)

if x:
    print("Yes, there is a match")
else:
    print('No match')



#ex 2
import re

txt = "The rain in Spain"

#Check if "ain" if present at the beginning of a WORD:
x = re.findall(r"\bain", txt)
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")



#ex 3
import re

txt = "The rain in Spain"

#Check if "ain" if present at the end of a WORD:
x = re.findall(r"ain\b", txt)
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")



#ex 4
import re

txt = "The rain in Spain"

#Check if the string contains any digitis (numbers from 0-9):

x = re.findall("\d", txt)
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("no mathc")



#ex 5
import re

txt  = "The rain in Spain"

x = re.findall("\D", txt)
print(x)

if x:
    print("Yes, there is at least ine match!")
else:
    print("No match")



#ex 6
import re

txt = "The rain in Spain"

#Return a match at every white-space character:

x = re.findall("\s", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")



#ex 7
import re

txt = "The rain in Spain"

#Return a match at every NON white-space character:

x = re.findall("\S", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")


#ex 8
import re

txt = "The rain in Spain"

#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):

x = re.findall("\w", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")



#ex 9
import re

txt = "The rain in Spain"

#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):

x = re.findall("\W", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")



#ex 10
import re

txt = "The rain in Spain"

#Check if the string ends with "Spain":

x = re.findall("Spain\Z", txt)

print(x)

if x:
    print("Yes, there is a match!")
else:
    print("No match")



#Sets
#ex 1

txt = "The rain in Spain"

#Check if the string has any a, r, or n characters:

x = re.findall("[arn]", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")



#ex 2
import re

txt = "The rain in Spain"

#Check if the string has any characters between a and n:

x = re.findall("[a-n]", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")



#ex 3
import re

txt = "The rain in Spain"

#Check if the string has other characters than a, r, or n:

x = re.findall("[^arn]", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")



#ex 4
import re

txt = "8 times before 11:45 AM"

#Check if the string has any digits:

x = re.findall("[0-9]", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")



#ex 5
import re

txt = "8 times before 11:45 AM"

#Check if the string has any two-digit numbers, from 00 to 59:

x = re.findall("[0-5][0-9]", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")



#ex 6
import re

txt = "8 times before 11:45 AM"

#Check if the string has any characters from a to z lower case, and A to Z upper case:

x = re.findall("[a-zA-Z]", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")



#ex 7
import re

txt = "8 times before 11:45 AM"

#Check if the string has any + characters:

x = re.findall("[+]", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")



#The findall() Function
#ex 1
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)



#ex 2
import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)



#The search() Function:
#ex 1
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())



#ex 2
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)



#THe split() Function:
#ex 1
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)



#ex 2
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)



#The sub() Function
#ex 1
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)



#ex 2
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)



#Match Object:
#ex 1
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object



#ex 2
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())



#ex 3
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)



#ex 4
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
