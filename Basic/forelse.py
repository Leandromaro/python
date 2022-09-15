def foo(my_list):
    for i in my_list:
        if i % 2 == 1:
            print(i)
        else:
            print("ELSE {}".format(i))
            break
    else:
        print(float('inf'))


foo([1, 5, 7, 9, 2])
