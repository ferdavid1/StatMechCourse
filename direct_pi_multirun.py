import random
import numpy as np 

def directpi(N):

	n_hits = 0

	for i in range(N):
		x,y = random.uniform(-1,1), random.uniform(-1,1)
		if x**2 + y**2 < 1:
			n_hits += 1

	return n_hits

n_trials = 1000
n_runs = 4000
pis = []
for run in range(n_runs):
	pis += [4*directpi(n_trials)/float(n_trials)]

# basically just try a bunch of times

# lets collect the mean/median!
print(np.mean(pis))
print(np.median(pis))
# mean =  3.1408 ---- eyy thats preddy gud
# median = 3.144 --- eyy preddy gudd