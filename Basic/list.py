# Python can store list with almost everythig 
my_favourite_things = [32, 'raindrops on roses', help()]

def printList(list):
	for x in list: 
		if (isinstance(x, int) or isinstance(x, str)):
			print(x)
		else:
			x

printList(my_favourite_things)