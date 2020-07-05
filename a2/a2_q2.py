from a2_q1 import *
from csp import *
from a2_q3 import *

def check_teams(graph, csp_sol):
	for i in range (len(csp_sol)):
		for j in range(1, len(csp_sol)):
			if csp_sol[i] == csp_sol[j]:
				if j in graph[i]:
					return False
	return True