# !/user/bin/env python
import random

def main():
	myfile = open('KargerMinCut.txt')
	adjlist = {}
	edges = []
	nodeId = 1
	for line in myfile:
		indices = line.split()
		indices = [int(i) for i in indices[1:]]
		indexSet = set()
		for item in indices:
			indexSet.add(item)
		adjlist[nodeId] = indexSet
		nodeId += 1
	tempEdgeSet = set()
	for nodeId in adjlist:
		for adjId in adjlist[nodeId]:
			if nodeId > adjId:
				tempEdgeSet.add((adjId, nodeId))
			else:
				tempEdgeSet.add((nodeId, adjId))
	for item in tempEdgeSet:
		edges.append(item)
	while len(edges) > 2:
	 	sel = random.randint(0,len(edges) - 1)
		edge = edges[sel]
		nodeA, nodeB = adjlist[edge[0]], adjlist[edge[1]]
		print edge[0], adjlist[edge[0]]
		print edge[1], adjlist[edge[1]]
		# nodeA.remove(edge[1])
		# nodeB.remove(edge[0])
		# nodeA = nodeA | nodeB
		# adjlist.pop(edge[1])
		# adjlist[edge[0]] = nodeA
		# edges.remove(edge)
				
if __name__ == "__main__":
	main()