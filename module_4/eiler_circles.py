# Кола Ейлера

import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# set1 = set([11, 12, 13, 14, 15, 16, 17, 18, 19])
# set2 = set([2, 4, 6, 8, 10, 12, 14, 16, 18])
# set3 = set([3, 6, 9, 12, 15, 18])

# venn3([set1, set2, set3], ('>10', 'Парні', 'Кратні 3'))
# plt.show()

set_1 = set()
set_2 = set()
set_3 = set()

for i in range(1, 31):
    if i % 2 == 0:
        set_1.add(i)
    if i % 5 == 0:
        set_2.add(i)
    if (i ** 0.5).is_integer():
        set_3.add(i)

print(f"Парні ({len(set_1)}): {set_1}")
print(f"Кратні 5 ({len(set_2)}): {set_2}")
print(f"Квадратні ({len(set_3)}): {set_3}")
venn3([set_1, set_2, set_3], ('Парні', 'Кратні 5', 'Квадратні'))
plt.show()
