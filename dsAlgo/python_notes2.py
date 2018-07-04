from collections import deque

# notes
# When writing code to search for items, it is common to use a generator function involving yield. This decouples
# the process of searching from the code that uses the results. 

# TODO: Look into yield, "in" in if statements and for loops

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# example use on a file
if __name__ == '__main__':
    with open('sample.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
                print('-'*20)
