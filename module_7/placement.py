import itertools
val = [1, 2, 3, 4]
perm_set = itertools.permutations(val, 2)
n = 0
for elem in perm_set:
    print(elem)
    n += 1
    print(n)

# Розміщення
# Порядок розташування предметів є важливим, тобто предмети відрізняються один від одного. Наприклад, у шухляді лежать шари чорного та білого кольору, ми витягаємо шари по черзі і не повертаємо їх назад.
# n! / (n-k)! = 12
