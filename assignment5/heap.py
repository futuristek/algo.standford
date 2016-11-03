'''
heap data structure
'''

class Heap:
	
	def parent(self, i):
		if i == 0:
			return -1
		else:
			return int((i+1)/2) - 1

	def left(self, i):
		return 2*i + 1

	def right(self, i):
		return 2*i + 2

	def max_heapify(self, i):
		l = self.left(i)
		r = self.right(i)
		a = self.a
		largest = i
		if l < len(a) and a[l] > a[i]:
			largest = l
		if r < len(a) and a[r] > a[largest]:
			largest = r
		if largest != i:
			a[i], a[largest] = a[largest], a[i]
			self.max_heapify(largest)

	def min_heapify(self, i):
		l = self.left(i)
		r = self.right(i)
		a = self.a
		smallest = i
		if l < len(a) and a[l] < a[i]:
			smallest = l
		if r < len(a) and a[r] < a[smallest]:
			smallest = r
		if smallest != i:
			a[i], a[smallest] = a[smallest], a[i]
			self.min_heapify(smallest)

	def build_max_heap(self, a):
		self.a = a
		s = len(a)
		for i in reversed(xrange(int(s/2))):
			self.max_heapify(i)
	
	def build_min_heap(self, a):
		self.a = a
		s = len(a)
		for i in reversed(xrange(int(s/2))):
			self.min_heapify(i)

	def test_heap(self):
		a = [1, 2, 3, 4 ,5, 6, 7, 8, 9, 10]
		print "Test:"
		print "array: " + str(a)
		self.build_max_heap(a[:])
		print "max heap: " + str(self.a)
		self.build_min_heap(a[:])
		print "min heap: " + str(self.a)

if __name__ == '__main__':
	heap = Heap()
	heap.test_heap()