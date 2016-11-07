import time
import sys
import threading

class Node:
	time = 0
	idByFinishTime = []
	treeEdgeCount = 0
	def __init__(self, id):
		self.id = id
		self.children = []
		self.d = 0
		self.f = 0
		self.color = 0

def DFSVISIT(G, u):
	Node.time += 1
	Node.treeEdgeCount += 1
	#print "	ID: "+ str(u.id) + " depth: " + str(Node.treeEdgeCount)
	u.d = Node.time
	u.color = 1
	for v in u.children:
		if v in G:
			if G[v].color == 0:
				DFSVISIT(G, G[v])
	u.color = 2
	Node.time += 1
	u.f = Node.time
	Node.idByFinishTime.append(u.id)
	#Node.treeEdgeCount += 1

def DFS(G):
	#node id starting from 1 not 0
	for id in xrange(1, len(G)+1):
		if id in G:
			if G[id].color == 0:
				#print "Entry ID: " + str(id)
				DFSVISIT(G, G[id])
	Node.idByFinishTime.reverse()

def DFSREVERSE(GT, orderd):
	listOfTreeEdgeCounts = []
	for id in orderd:
		if id in GT:
			if GT[id].color == 0:
				Node.treeEdgeCount = 0
				DFSVISIT(GT, GT[id])
				listOfTreeEdgeCounts.append(Node.treeEdgeCount)
	return listOfTreeEdgeCounts

def SCC():

	print "Loading scc.txt ... "
	tic = time.clock()
	myfile = open('scc.txt')
	G = {}
	GT = {}
	for line in myfile:
		E = line.split()
		E[0], E[1] = int(E[0]), int(E[1])
		if E[0] in G:
			G[E[0]].children.append(E[1])
		else:
			node = Node(E[0])
			node.children.append(E[1])
			G[E[0]] = node
		if E[1] not in G:
			node = Node(E[1])
			G[E[1]] = node
		#transpose graph
		ET = []
		ET.append(E[1])
		ET.append(E[0])
		if ET[0] in GT:
			GT[ET[0]].children.append(ET[1])
		else:
			node = Node(ET[0])
			node.children.append(ET[1])
			GT[ET[0]] = node
		if ET[1] not in GT:
			node = Node(ET[1])
			GT[ET[1]] = node
	myfile.close()

	toc = time.clock() - tic
	print "Loading finishded in: " + str(toc) + " s"

	print "DFS 1st pass... "
	tic = time.clock()
	
	DFS(GT)

	toc = time.clock() - tic
	print "DFS 1st pass finishded in: " + str(toc) + " s"
	
	idOrderedByFinishTime = {}
	for key, value in GT.iteritems():
		idOrderedByFinishTime[value.f] = key

#	print Node.idByFinishTime

 	# for key, value in GT.iteritems():
		# print key, value.children

	print "DFS 2nd pass ... "
	tic = time.clock()

	listOfTreeEdgeCounts = DFSREVERSE(G, Node.idByFinishTime)
	
	toc = time.clock() - tic
	print "DFS 2nd pass finishded in: " + str(toc) + " s"

	myfile = open('scc_sizes.txt', 'w')

	for item in sorted(listOfTreeEdgeCounts, reverse=True):
		myfile.write(str(item)+'\n')

	myfile.close()

if __name__ == '__main__':
	sys.setrecursionlimit(2 ** 20)
	threading.stack_size(67108864)
	thread = threading.Thread(target=SCC)
	thread.start()
	#SCC()
	
