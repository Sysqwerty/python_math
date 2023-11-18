import itertools
val = [1, 2, 3, 4]
com_set = itertools.combinations(val, 2)
n = 0
for elem in com_set:
    print(elem)
    n += 1
    print(n)

# Комбінації
# скількома способами можна отримати k предметів із n можливих
# n! / (k!(n-k))! = 6
