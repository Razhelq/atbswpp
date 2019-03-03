import time, subprocess


time_left = 10
while time_left > 0:
    print(time_left)
    time.sleep(1)
    time_left = time_left - 1

subprocess.Popen(['start', 'alarm.wav'], shell=True)

