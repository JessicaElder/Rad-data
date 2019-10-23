#Loop test
import time
import math 

timeout = 5
timeout_start = time.time()
n = 0

while time.time() < timeout_start + timeout:
	if n <= 10:
		n += 1
		print(n)
		time.sleep(0.01)
#print(n)
