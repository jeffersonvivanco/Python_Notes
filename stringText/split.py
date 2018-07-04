import re

line = 'java, c++, c,  python; js,html, php  old'

# the seperator is a semicolon, comma, or whitespace followed by any amount of extra whitespace
fields = re.split(r'(;|,|\s)\s*', line) 
print(fields)

# getting the split characters might be useful in certain contexts. 
# ex: maybe you need the split characters later on to reform the string 
# note: look up what is ::2 in an array

values = fields[::2]
delimiters = fields[1::2] + ['']

# Reform the line using the same delimiters
joinedString = ''.join(v+d for v, d in zip(values, delimiters))

# if you don't want the seperator characters in the result, but still need to use parentheses to group
# parts of the regular expression pattern, make sure you use a non capture group, specified as (?:...)
noSeperatorGroup = re.split(r'(?:,|;|\s)\s*', line)
print(noSeperatorGroup)

