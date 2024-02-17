#ex 1
import re

def match_pattern(txt):
    patterns = '^a(b*)$'
    if re.search(patterns, txt):
        return 'Found a match!'
    else:
        return 'No matched!'

txt = input()
print(match_pattern(txt))



#ex 2
import re

def match_pattern(txt):
    pattern = r'ab'
    if re.match(pattern, txt):
        return "Found a match"
    else:
        return "No matched!"

txt = input()
print(match_pattern(txt))



# ex 3
import re

def sequences_of_lowercase(txt):
    pattern = '^[a-z] + _[a-z] + $'
    if re.search(pattern, txt):
        return "Found a match"
    else:
        return "No matched"

txt = input()
print(sequences_of_lowercase(txt))



#ex 4
import re

def sequence_of_oneuppercase(txt):
    pattern = '[A-Z]+[a-z]+$'
    if re.search(pattern, txt):
        return "Found a match"
    else:
        return "No matched"
    
txt = input()
print(sequence_of_oneuppercase(txt))



#ex 5
import re

def search_match(txt):
    pattern = 'a.*?b$'
    if re.search(pattern, txt):
        return "Found a match"
    else:
        return "No matched"
    
txt = input()
print(search_match(txt))



#ex 6
import re

txt = input()
print(re.sub("[ ,.]", ":", txt))



#ex 7
import re

def snake_to_camel(txt):
    return ''.join(i.capitalize() or '_' for i in txt.split('_'))

txt = input()
print(snake_to_camel(txt))



#ex 8
import re

def split_string(txt):
    pattern = '[A-Z][^A-Z]*'
    return re.findall(pattern, txt)

txt = input()
print(split_string(txt))



#ex 9
import re

def capital_words_spaces(txt):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", txt)

txt = input()
print(capital_words_spaces(txt))



#10
import re

def camel_to_snake(txt):
    txt = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', txt)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', txt).lower()

txt = input()
print(camel_to_snake(txt))

