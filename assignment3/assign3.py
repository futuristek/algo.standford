# !/user/bin/env python
from random import randrange
import math
import copy
def contract(adjlist):
	if len(adjlist) == 2:
		return adjlist
	totalnum, anode, bnode = 0, 0, 0
	for key, value in adjlist.iteritems():
		totalnum += len(value)
	#randnum = random.randint(1, totalnum)
	randnum = randrange(totalnum) + 1
	for key, value in adjlist.iteritems():
		if randnum <= len(value):
			anode, bnode = key, value[randnum - 1]
			break
			#print randnum, anode, bnode, value
		else:
			randnum -= len(value)
	adjlist[anode] = [v for v in adjlist[anode] if v != bnode]
	adjlist[bnode] = [v for v in adjlist[bnode] if v != anode]
	for node in adjlist[bnode]:
		for idx in xrange(0, len(adjlist[node])):
			if adjlist[node][idx] == bnode:
				adjlist[node][idx] = anode
	adjlist[anode].extend(adjlist[bnode])
	adjlist.pop(bnode)
	return contract(adjlist)

def main():
	myfile = open('KargerMinCut.txt')
	#myfile = open('test.txt')
	adjlist = {}
	for line in myfile:
		indices = line.split()
		adjlist[int(indices[0])] = [int(i) for i in indices[1:]]
	minCut = 0
	numnodes = len(adjlist)
	for i in xrange(0, numnodes):
	#for i in xrange(0, 1):
		result = contract(copy.deepcopy(adjlist))
		while len(result) > 2:
		 	result = contract(result)
		keys = result.keys()
		assert len(result[keys[0]]) == len(result[keys[1]])
		if len(result[keys[0]]) < minCut or i == 0:
			minCut = len(result[keys[0]])
		print i
	print "Mint cut = "+str(minCut)

if __name__ == "__main__":
	main()