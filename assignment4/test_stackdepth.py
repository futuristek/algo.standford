import time
import sys
sys.setrecursionlimit(20000)
print sys.getrecursionlimit()

sum = 0

def add(n):
	if n > 1:
		print n
		add(n - 1)
	else:
		return

if __name__ == "__main__":
	add(22781)
	print sum