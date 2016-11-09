'''
Exercise 5: Dijkstra algorithm simpler version with O(m*n)
'''
import sys
G, A, X = [], [], []

def read():
	global A, X
	#with open('dijkstraData.txt') as f:
	with open('testData.txt') as f:	
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
			X.append(int(t[0]) - 1)
	A = [sys.maxsize]*len(G)

def minDist():
	m, i = A[X[0]], 0
	for n in range(len(X)):
		if A[X[n]] < m:
			m, i = A[X[n]], n
	return m, i

def dij(s):
	A[s] = 0
	while len(X) > 0:
		m, i = minDist()
		for n in G[X[i]]:
			if m + n[1] < A[n[0]]:
				A[n[0]] = m + n[1]
		X[-1], X[i] = X[i], X[-1]
		X.pop()

def myprint():
	print("Dijkstra min distance to source ...")
	#print(A[7 - 1],A[37 - 1],A[59 - 1],A[82 - 1],A[99 - 1],A[115 - 1],A[133 - 1],A[165 - 1],A[188 - 1],A[197 - 1], sep=',')
	print(A)

def main():
	read()
	dij(0)
	myprint()

if __name__ == '__main__':
	main()