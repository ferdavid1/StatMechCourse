import random

histo = [0,0,0,0,0,0,0,0,0]
neighbor = [[1,3,0,0], [2,4,0,1], [2,5,1,2],
			[4,6,3,0], [5,7,3,1], [5,8,4,2], 
			[7,6,6,3], [8,7,6,4], [8,8,7,5]]
weight = [3,0.5, 1, 0.5, 1,0.5, 2,0.5,1]
'''
those were the respective weights were each square has
different likelihoods of being landed on
'''
pos = 8 # current position
n_iter = 100000000
for i in range(n_iter):
	new_pos = neighbor[pos][random.randint(0,3)]
	if random.random() < weight[new_pos] / weight[pos]:
		pos = new_pos
	histo[pos] += 1

norm = sum(weight)
print('comparison: weight, histogram')
for k in range(9):
	print('site: ' + k + 'weight: ' + str(weight[k]) + 'histo: ' + str(norm*histo[k] / float(n_iter)))

