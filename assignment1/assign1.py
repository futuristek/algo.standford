# !/usr/bin/env python
numInversions = 0

def merge_and_count_inversions(a):
	global numInversions
	size = len(a)
	if size == 1:
		return a 
	b = a[:size/2]
	c = a[size/2:]
	sorted_b = merge_and_count_inversions(b)
	sorted_c = merge_and_count_inversions(c)
	d = []

	#No inversion between sorted_b and sorted_c
	if sorted_b[-1] < sorted_c[0]:
		d = sorted_b + sorted_c
		return d

	i = j = 0
	left = []
	for index in range(0, size):
		if sorted_b[i] <= sorted_c[j]:
			d.append(sorted_b[i])
			i += 1
			if i == len(sorted_b):
				left = sorted_c[j:]
				break 
		else:
			d.append(sorted_c[j])
			numInversions += (len(sorted_b) - i)
			j += 1
			if j == len(sorted_c):
				left = sorted_b[i:]
				break
	d += left

	return d

def main():
	myfile = open('IntegerArray.txt')
	array = []
	for item in myfile:
		array.append(int(item))
	sortedArray = merge_and_count_inversions(array)
	tofile = open('SortedArray.txt', 'w')
	for item in sortedArray:
		tofile.write(str(item)+'\n')
	tofile.close();
	myfile.close();
	print numInversions

if __name__ == "__main__":
	main()
