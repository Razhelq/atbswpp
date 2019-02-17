# stopwatch.py - A simple stopwatch program.


import time


# Display the program's instructions.
print('Press enter to begin. Afterwards, press Enter to "click" the stopwatch. Press Ctrl-C to quit.')
input()                     # Press enter to begin
print('Started.')
start_time = time.time()    # get the first lap's start time
last_time = start_time
lap_num = 1

# Start tracking the lap times.
try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        print('Lap #{}: {}s ({}s)'.format(lap_num, total_time, lap_time), end='')
        lap_num += 1
        last_time = time.time() # resets the last lap time
except:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')

