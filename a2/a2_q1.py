import random 

# returns a new random graph with n nodes numbered 0 to n−1
# such that every different pair of nodes is connected with probability p. 
# Assume n > 1, and 0 <= p <= 1

def rand_graph(p,n):
	graph = {}

	for x in range(n):
		graph[x] = []

	for y in range(n):
		for z in range(y+1, n):
			if (random.random() < p):
				graph[y].append(z)
				graph[z].append(y)
	return graph
print(rand_graph(0.5,5))