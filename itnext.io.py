import time

chars = 'ABCDEFGH'
loop = range(1, len(chars) + 1)

for idx in loop:
    print(chars[:idx])
    time.sleep(.5)