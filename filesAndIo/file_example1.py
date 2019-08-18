import os
# read the entire file as a single string
# with open('test.txt', 'rt') as f:
#     data = f.read()

# iterate over the lines of the file
lines = [] # array used to store the lines
os.path.basename('filesAndIo/')
with open('test.txt', 'rt') as f:
    for line in f:
        lines.append(line)
print(lines)

# write chunks of text data
with open('test.txt', 'wt') as f:
    f.write('Hello Jeff, this is computer')


# # redirect print statement to a file
# with open('test.txt', 'wt') as f:
#     print('test print statement', file=f)
#
# # append to the end of a file
# with open('test.txt', 'at') as f:
#     print('test print statement 2 should appear with the first one', file=f)
