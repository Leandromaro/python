def elementwise_greater_than(L, thresh):
    return [n>thresh for n in L ]

print(elementwise_greater_than([1, 2, 3, 4], 2))

