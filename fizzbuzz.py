import sys

def fizzbuzz(n):
	count=1
	while (count<=n):
		if (count%3 == 0) and (count%5 == 0): 
			print "fizzbuzz"
			count=count+1
		elif count%3 == 0:
			print "fizz"
			count=count+1
		elif count%5 == 0:
			print "buzz"
			count=count+1
		else:
			print count
			count=count+1

if __name__ == '__main__':
	n=int(sys.argv[1])
	fizzbuzz(n)
