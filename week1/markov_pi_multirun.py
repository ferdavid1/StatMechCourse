import random
import numpy as np

def markov_pi(N, delta):
	x,y = 1,1
	n_hits = 0

	for i in range(N):
		delta_x, delta_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
		if abs(x+delta_x) < 1.0 and abs(y+delta_y) < 1.0:
			x,y = x+delta_x, y+delta_y
		if x**2 + y**2 < 1.0:
			n_hits += 1
	return n_hits

n_trials = 10000
n_runs = 4000
delta = 0.1
pis = []
for run in range(n_runs):
	pis += [4*markov_pi(n_trials, delta)/float(n_trials)]

print("Mean pi value:", np.mean(pis)) # 3.1197275
print("Median pi value:", np.median(pis)) # 3.123
