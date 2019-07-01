
it = map(lambda x: print(x**2, end=' '), [1, 2, 3, 4])
next(it)
next(it)
next(it)
next(it)

print('\n========================')

lst = list(map(lambda x: x**2, [1, 2, 3, 4]))
print(lst)

print('========================')

list(map(lambda x: print(x**2, end=' '), [1, 2, 3, 4]))

print('\n========================')

lst = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))
print(lst)
