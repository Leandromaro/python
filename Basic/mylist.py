my_list = [True, True, True]
def foo(my_list):
    try:
        return my_list[1] + my_list[2] == my_list[0]
    except (IndexError, TypeError):
    	#print("test")
        return True

print(foo(my_list))
