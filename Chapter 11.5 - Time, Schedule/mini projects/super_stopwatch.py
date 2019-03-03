# stopwatch.py - A simple stopwatch program.


import time, pyperclip


# Display the program's instructions.
import pyperclip as pyperclip

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
        ret_string = ('Lap #{}: {}s ({}s)'.format(str(lap_num).rjust(2), str(total_time).rjust(5), str(lap_time).rjust(5)))
        print(ret_string, end='')
        pyperclip.copy(ret_string)
        lap_num += 1
        last_time = time.time() # resets the last lap time
except:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')

