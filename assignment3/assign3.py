# !/user/bin/env python
import random

def main():
	myfile = open('KargerMinCut.txt')
	adjlist = {}
	nodeId = 1
	for line in myfile:
		indices = line.split()
		indices = [int(i) for i in indices[1:]]
		indexSet = set()
		for item in indices:
			indexSet.add(item)
		adjlist[nodeId] = indexSet
		nodeId += 1
	edgeSet = set()
	for nodeId in adjlist:
		for adjId in adjlist[nodeId]:
			if nodeId > adjId:
				edgeSet.add((adjId, nodeId))
			else:
				edgeSet.add((nodeId, adjId))
	fakeRnd = 0
	edge = (0, 0)
	while len(edgeSet) > 2:
	 	#sel = random.randint(0,len(edgeSet) - 1)
		sel = fakeRnd
		counter = 0
		for item in edgeSet:
			if counter == sel:
				edge = item
			counter += 1
		print "Contracted edge: "+str(sel)
		print edge
		nodeA = adjlist[edge[0]]
		nodeB = adjlist[edge[1]]								
		nodeA = nodeA | nodeB		#merge B's adjacent nodes into A's
		adjlist[edge[0]] = nodeA	#updating A in adjacent list
		adjlist.pop(edge[1])		#remove B from adjacnet list
		print "before remove:"+str(len(edgeSet))
		edgeSet.remove(edge)		#remove the contracted edge
		print "after remove:"+str(len(edgeSet))
		remList = []
		addList = []
		for item in edgeSet:			#all Bs in edge set are replaced with A
			if item[0] == edge[1]:
				remList.append(item)
				print "if: "+str(item)
				if edge[0] < item[1]:
					addList.append((edge[0], item[1]))
				else:
					addList.append((item[1], edge[0]))
			elif item[1] == edge[1]:
				remList.append(item)
				print "else: "+str(item)
				if item[0] < edge[0]:
					addList.append((item[0], edge[0]))
				else:
					addList.append((edge[0], item[0]))
		print remList
		print addList
		for item in remList:
			edgeSet.remove(item)
		for item in addList:
			if item[0] != item[1]:
				edgeSet.add(item)
				
		#print edge[0], adjlist[edge[0]]
		#print edge[1], adjlist[edge[1]]
		# nodeA.remove(edge[1])
		# nodeB.remove(edge[0])
		# nodeA = nodeA | nodeB
		# adjlist.pop(edge[1])
		# adjlist[edge[0]] = nodeA
		fakeRnd += 1
				
if __name__ == "__main__":
	main()