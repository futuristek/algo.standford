def test(mydict):
	mydict[3] = 'b'

def main():
	anodict = {}
	anodict[1] = 'a'
	anodict[2] = 'b'
	test(anodict.copy())
	print anodict

if __name__ == '__main__':
	main()