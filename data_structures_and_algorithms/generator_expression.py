# using generator-expressions
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(s)

# determine if any .py files exist in a directory
import os
# direcory below is up one more level dir
files = os.listdir('../');
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python!')
