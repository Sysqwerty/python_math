import itertools
val = [1, 2, 3, 4]
perm_set = itertools.permutations(val)
n = 0
for elem in perm_set:
    print(elem)
    n += 1
    print(n)

# Перестановки
# За визначенням, перестановка дорівнює числу способів, за допомогою яких можна побудувати різні послідовності з 𝑛 предметів
# n! = 24
