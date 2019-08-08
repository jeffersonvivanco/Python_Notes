import time, sys, random


# progress indicator
def loading():
    print('Loading...')
    for i in range(0, 100):
        time.sleep(.1)
        sys.stdout.write(u'\u001b[1000D{0}%'.format(i + 1))
        sys.stdout.flush()
    print('\nDone!')


# progress bar
def loading_pb():
    print('loading...')
    for i in range(0, 100):
        time.sleep(.1)
        width = int((i + 1)/4)
        bar = '[' + '#' * width + ' ' * (25 - width) + ']'
        # every iteration of the loop, the entire row is erased and a new version of the ASCII bar is drawn
        sys.stdout.write(u'\u001b[1000D{0}'.format(bar))
        sys.stdout.flush()
    print()


# multiple progress bar
def loading_mpb(count):
    all_progress = [0] * count
    print('\n' * 5, end='') # make sure we have space to draw the bars
    while any(x < 100 for x in all_progress):
        time.sleep(0.01)
        # Randomly increment one of our progress values
        unfinished = [(i, v) for (i, v) in enumerate(all_progress) if v < 100]
        index, _ = random.choice(unfinished)
        all_progress[index] += 1

        # Draw the progress bars
        sys.stdout.write(u'\u001b[1000D') # move left
        sys.stdout.write(u'\u001b[{0}A'.format(count)) # Move up
        for progress in all_progress:
            width = int(progress / 4)
            print('[' + '#' * width + ' ' * (25 - width) + ']')


# loading()
# loading_pb()
loading_mpb(5)
