x = [2,1]
y = [2,1]
z = False
if x == y:
	print "sorted(x) ", sorted(x)
	print "sorted(y) ", sorted(y)
	if sorted(x) == sorted(y):
		print "sort(x) ", x.sort()
		print "sort(y) ", y.sort()
		if x.sort() == y.sort():
			z =  x.sort() == sorted(y)
print z