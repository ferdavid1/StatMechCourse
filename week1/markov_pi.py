import random

'''
At position x,y you move by small random displacement
delta_x, delta_y - which can be positive or negative.
'''

x,y = 1,1
delta = 0.1
n_trials = 4000
n_hits = 0

for i in range(n_trials):
	del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
	if abs(x + del_x) < 1 and abs(y+del_y) < 1:
		x,y = x + del_x, y + del_y
		# if not within square, stay where u are
		# if within square, advance delta amount
	if x**2 + y**2 < 1:
		n_hits += 1
		# if within circle, its a hit!

print(4*n_hits/float(n_trials))
# 3.245