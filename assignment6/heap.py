'''
heap data structure
'''
class Heap:
	def __init__(self, a):
		self.a = a

	def parent(self, i):
		if i == 0:
			return -1
		else:
			return int((i+1)/2) - 1

	def left(self, i):
		return 2*i + 1

	def right(self, i):
		return 2*i + 2

	def heapify(self, i):
		raise NotImplementedError("Please Implement this method")
	
	def build_heap(self):
		s = len(self.a)
		for i in reversed(range(int(s/2))):
			self.heapify(i)

	def top(self):
		return self.a[0]

	def size(self):
		return len(self.a)

	def print(self):
		print(self.a)

class MaxHeap(Heap):

	def heapify(self, i):
		l = Heap.left(self, i)
		r = Heap.right(self, i)
		a = self.a
		largest = i
		if l < len(a) and a[l] > a[i]:
			largest = l
		if r < len(a) and a[r] > a[largest]:
			largest = r
		if largest != i:
			a[i], a[largest] = a[largest], a[i]
			self.heapify(largest)
	
	def bubble_up(self, i):
		if i == 0:
			return
		else:
			p = Heap.parent(self, i)
			if self.a[i] <= self.a[p]:
				return
			else:
				self.a[i], self.a[p] = self.a[p], self.a[i]
				self.bubble_up(p)

	def insert(self, k):
		self.a.append(k)
		t = len(self.a) - 1
		self.bubble_up(t)

	def bubble_down(self, i):
		l = Heap.left(self, i)
		if l >= len(self.a):
			return
		else:
			r = Heap.right(self, i)
			largest = i
			if self.a[l] > self.a[i]:
				largest = l
			if r < len(self.a) and self.a[r] > self.a[largest]:
				largest = r
			if largest == i:
				return
			else:
				self.a[i], self.a[largest] = self.a[largest], self.a[i]
				self.bubble_down(largest)

	def extract(self):
		tmp = self.a[0]
		self.a[0] = self.a[-1]
		self.a.pop()
		self.bubble_down(0)
		return tmp

class MinHeap(Heap):

	def heapify(self, i):
		l = Heap.left(self, i)
		r = Heap.right(self, i)
		a = self.a
		smallest = i
		if l < len(a) and a[l] < a[i]:
			smallest = l
		if r < len(a) and a[r] < a[smallest]:
			smallest = r
		if smallest != i:
			a[i], a[smallest] = a[smallest], a[i]
			self.heapify(smallest)

	def bubble_up(self, i):
		if i == 0:
			return
		else:
			p = Heap.parent(self, i)
			if self.a[i] >= self.a[p]:
				return
			else:
				self.a[i], self.a[p] = self.a[p], self.a[i]
				self.bubble_up(p)

	def insert(self, k):
		self.a.append(k)
		t = len(self.a) - 1
		self.bubble_up(t)

	def bubble_down(self, i):
		l = Heap.left(self, i)
		if l >= len(self.a):
			return
		else:
			r = Heap.right(self, i)
			smallest = i
			if self.a[l] < self.a[i]:
				smallest = l
			if r < len(self.a) and self.a[r] < self.a[smallest]:
				smallest = r
			if smallest == i:
				return
			else:
				self.a[i], self.a[smallest] = self.a[smallest], self.a[i]
				self.bubble_down(smallest)

	def extract(self):
		tmp = self.a[0]
		self.a[0] = self.a[-1]
		self.a.pop()
		self.bubble_down(0)
		return tmp

	# update the key of any index, bubble_up or bubble_down
	def update(self, i, k):
		if i < 0 or i >= len(self.a): return
		self.a[i] = k		
		l = Heap.left(self, i)
		r = Heap.right(self, i)
		p = Heap.parent(self, i)
		if p > -1 and self.a[p] > k:
			self.a[p], self.a[i] = self.a[i], self.a[p]
			self.bubble_up(p)
		else:
			smallest = 0
			if l < len(self.a) and self.a[l] < k:
				smallest = k
			if r < len(self.a) and self.a[r] < k:
				smallest = r
			if smallest != 0:
				self.a[0], self.a[smallest] = self.a[smallest], self.a[0]
				self.buble_down(smallest)

if __name__ == '__main__':
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	print("array: ", str(b))
	min_heap = MinHeap(b[:])
	max_heap = MaxHeap(b[:])
	min_heap.build_heap()
	max_heap.build_heap()
	print("min heap: ", str(min_heap.a))
	print("insert 0: ")
	min_heap.insert(0)
	print("result: ", str(min_heap.a))
	print("extract min: ", str(min_heap.extract()))
	print("result: ", str(min_heap.a))
	print("max heap: ", str(max_heap.a))	
	print("insert 12: ")
	max_heap.insert(12)
	print("result: ", str(max_heap.a))
	print("extract max: ", str(max_heap.extract()))
	print("result: ", str(max_heap.a))
	print("update min heap: ")
	min_heap = MinHeap(b[:])
	min_heap.update(5, 6.5)
	print("result: ", str(min_heap.a))
