'''
Exercise 5: Dijkstra algorithm with O(m*n) running time
'''
import sys

A, G, H, = [], [], []

class Node:
	def __init__(self, v, w):
		self.v = v
		self.w = w

class MinHeap:
	def __init__(self, a):
		self.a = a[:]
		self.pos = [-1]*len(self.a)
		for idx in range(len(self.a)):
			self.pos[idx] = idx

	def parent(self, idx):
		return int((idx+1)/2) - 1

	def left(self, idx):
		return 2*idx + 1

	def right(self, idx):
		return 2*idx + 2

	def bubble_up(self, idx):
		if idx == 0: return
		p = self.parent(idx)
		if self.a[idx].w > self.a[p].w:
			return
		else:
			self.swap(idx, p)
			self.bubble_up(p)

	def bubble_down(self, idx):
		l, r, smallest = self.left(idx), self.right(idx), idx
		if l < len(self.a) and self.a[l].w < self.a[idx].w:
			smallest = l
		if r < len(self.a) and self.a[r].w < self.a[smallest].w:
			smallest = r
		if smallest == idx:
			return
		else:
			self.swap(idx, smallest)
			self.bubble_down(smallest)

	def extract_min(self):
		v, w = self.a[0].v, self.a[0].w 
		self.swap(0, len(self.a) - 1)
		self.pos[v] = -1
		self.a.pop()
		self.bubble_down(0)
		return v, w

	def swap(self, i, j):
		self.a[i], self.a[j] = self.a[j], self.a[i]
		v = self.a[i].v
		u = self.a[j].v
		self.pos[v], self.pos[u] = self.pos[u], self.pos[v]

	def get_pos(self, v):
		return self.pos[v]

	def update(self, v, weight):
		idx = self.get_pos(v)
		self.a[idx].w = weight
		p = self.parent(idx)
		if p > -1 and self.a[idx].w < self.a[p].w:
			self.swap(idx, p)
			self.bubble_up(p)
		else:
			l, r = self.left(idx), self.right(idx)
			smallest = idx
			if l < len(self.a) and self.a[l].w < self.a[idx].w:
				smallest = l
			if r < len(self.a) and self.a[r].w < self.a[smallest].w:
				smallest = r
			if smallest != idx:
				self.swap(idx, smallest)
				self.bubble_down(smallest)

	def init(self, s):
		self.a[s].w = 0

	def get_weight(self, v):
		idx = self.get_pos(v)
		return self.a[idx].w

	def get_size(self):
		return len(self.a)

def read(file_name):
	global A
	with open(file_name) as f:
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
			v = int(t[0]) - 1
			node = Node(v, sys.maxsize)
			H.append(node)
		A = [sys.maxsize]*len(G)

def dij():
	read('dijkstraData.txt')
	heap = MinHeap(H)
	heap.init(0)
	while heap.get_size() > 0:
		v, w = heap.extract_min()
		A[v] = w
		for u in G[v]:
			score = w + u[1]
			if heap.get_pos(u[0]) != -1 and score < heap.get_weight(u[0]):
				heap.update(u[0], score)

def myprint():
	print("Dijkstra min distance to source ...")
	print(A[7 - 1],A[37 - 1],A[59 - 1],A[82 - 1],A[99 - 1],A[115 - 1],A[133 - 1],A[165 - 1],A[188 - 1],A[197 - 1], sep=',')

if __name__ == '__main__':
	dij()
	myprint()