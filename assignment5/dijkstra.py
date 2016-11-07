'''
Exercise 5: Dijkstra algorithm with O(m*n) running time
'''
G, A, X = [], [], []
E = {}

def read():
	with open('dijkstraData.txt') as f:
	#with open('testData.txt') as f:	
		for line in f:
			adjl = []
			line = line.rstrip('\r\n')
			line = line.rstrip()
			t = line.split('\t')
			for e in t[1:]:
				temp = e.split(',')
				n_d = list(map(int, e.split(',')))
				#force node index starting from 0
				n_d[0] -= 1
				adjl.append(n_d)
			G.append(adjl)
	A = [-1]*len(G)

def minScore(E):
	keys = list(E.keys())
	w = keys[0]
	d = E[w]
	for k, v in E.items():
		if v < d:
			w, d = k, v
	return w, d

def dij(s):
	A[s] = 0
	X.append(s)
	adjl = G[s]
	for i in adjl:
		E[i[0]] = i[1]
	while len(X) < len(G):
		w, d = minScore(E)
		A[w] = d
		X.append(w)
		del E[w]
		for i in G[w]:
			if A[i[0]] != -1:
				continue
			t = A[w] + i[1]
			if i[0] in E:
				if t < E[i[0]]:
					E[i[0]] = t
			else:
				E[i[0]] = t

def myprint():
	print("Dijkstra min distance to source ...")
	print(A[7 - 1],A[37 - 1],A[59 - 1],A[82 - 1],A[99 - 1],A[115 - 1],A[133 - 1],A[165 - 1],A[188 - 1],A[197 - 1], sep=',')

def main():
	read()
	dij(0)
	myprint()

if __name__ == '__main__':
	main()