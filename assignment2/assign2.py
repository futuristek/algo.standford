# !/usr/bin/env python
# This is an in-memory implementation of quick-sort

array = []
numComps = 0

def swap(i, j):
	temp = array[i]
	array[i] = array[j]
	array[j] = temp

def comparison_first(l, r):
	size = r - l + 1
	p = l
	i = l + 1
	findLess = False
	for j in range(l+1, r+1):
		if array[j] < array[p]:
			swap(j, i)				
			i += 1
			findLess = True
	if findLess == True:
		swap(p, i - 1)
		p = i - 1
	return p

def comparison_last(l, r):
	swap(l, r)
	size = r - l + 1
	p = l
	i = l + 1
	findLess = False
	for j in range(l+1, r+1):
		if array[j] < array[p]:
			swap(j, i)				
			i += 1
			findLess = True
	if findLess == True:
		swap(p, i - 1)
		p = i - 1
	return p

def comparison_median(l, r):
	size = r - l + 1
	a = array[l]
	b = array[(r+l)/2]
	c = array[r]
	if (b > a and b < c) or (b > c and b < a):
		swap(l, (r+l)/2)
	elif (c > a and c < b) or (c > b and c < a):
		swap(l, r)
	p = l
	i = l + 1
	findLess = False
	for j in range(l+1, r+1):
		if array[j] < array[p]:
			swap(j, i)				
			i += 1
			findLess = True
	if findLess == True:
		swap(p, i - 1)
		p = i - 1
	return p


def quicksort(l, r):
	size = r - l + 1
	if size <= 1:
		return
	else:
		global numComps
		numComps += size - 1
	#p = comparison_first(l, r)
	p = comparison_last(l, r)
	#p = comparison_median(l, r)
	quicksort(l,p-1)
	quicksort(p+1, r)

def main():
	myfile = open('quicksort.txt')
	global array
	for item in myfile:
		array.append(int(item))
	quicksort(0, len(array) - 1)
	outfile = open('sorted.txt', 'w')
	for number in array:
		outfile.write(str(number)+'\n')
	myfile.close()
	outfile.close()
	print "Number of comparisons = " + str(numComps)
if __name__ == "__main__":
	main()