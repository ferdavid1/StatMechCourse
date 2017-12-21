import random

'''
pi/4 = ratio of area of the circle / area of square
made up of the edges of the circle

area_circle/area_square * 4 == hits/trials * 4 == pi
'''

n_trials = 4000
n_hits = 0

for x in range(n_trials):
	x,y = random.uniform(-1, 1), random.uniform(-1, 1) # x and y coordinates
	if x**2 + y**2 < 1: # x^2 + y^2 = 1 is the circle formula 
		n_hits += 1 # if within a circle, is hit

print(4*n_hits / float(n_trials))
# this returns 3.165

# if given more trials, number would get closer to real pi
	# when given 100,000,000 trials, pi = 3.14182796