text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re
# simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

# if you are going to perform a lot of matches using the same pattern, it usually pays to precompile the regular expression
# pattern into a pattern object first. ex:
datepat = re.compile(r'\d+/\d+/\d+')
if(datepat.match(text2)):
    print('yes')
else:
    print('no')

# using capture groups
datepat2 = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat2.match(text1)
print(m.group(0))
print(m.group(1))
print(m.groups())

# using sub function to find and replace
# the backslash digits refer to the capture group numbers
text = 'Today is 11/27/2012. PyCon starts 3/13/2013'
textR = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(textR)

# performing case-insensitive matching
caseIText = 'UPPER PYTHON, lower python, Mixed Python';
allPython = re.findall('python', caseIText, flags=re.IGNORECASE)



# finding the shortest match
# the '*' is greedy and will perform the longest possible match, to fix this add '?' modifier
# '?' makes the matching non greedy and produces the shortest match instead
str_pat = re.compile(r'\"(.*)\"')
sMatchText = 'Computer says "no." Phone says "yes."'
allSMatch = str_pat.findall(sMatchText)

