import bisect
 
a = []
with open('input.txt') as f:
	a = [int(l) for l in f]
	a.sort()

ret = set()
for x in a:
	lower = bisect.bisect_left(a, -10000 - x)
	uppper = bisect.bisect_right(a, 10000 - x)
	for y in a[lower:uppper]:
		if x != y and x + y not in ret:
			ret.add(x + y)

print(len(ret))