def high_order_function(fun, first = None, second = None):
	if None not in (first, second):
		if (fun(first, second)):
			print("mayor")
		else: 
			print("menor")
	else: 
		fun()	

def greet(who= "leandro"):
	print("hi", who)

def may(first, second):
	return first >= second

high_order_function(may, 5, 9)
high_order_function(greet)

