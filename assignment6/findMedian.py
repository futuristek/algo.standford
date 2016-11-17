from heap import MinHeap, MaxHeap
from math import floor
import sys
#invariant: maintain min heap size = floor(n/2), median is the the max in max heap
with open('Median.txt') as f:
#with open('median10_test.txt') as f:
	a = [int(l) for l in f]
	minHeap = MinHeap([])
	maxHeap = MaxHeap([])
	medians = []
	for i in range(len(a)):
		if minHeap.size() == 0 and maxHeap.size() == 0:
			maxHeap.insert(a[i])
		else:
			if a[i] < maxHeap.top():
				maxHeap.insert(a[i])
			else:
				minHeap.insert(a[i])
			if minHeap.size() > floor((i+1)/2):
				maxHeap.insert(minHeap.extract())
			elif minHeap.size() < floor((i+1)/2):
				minHeap.insert(maxHeap.extract())
		medians.append(maxHeap.top())
	print(sum(medians)%10000)