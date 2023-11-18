import numpy as np
from numpy import linalg as la


a = np.array([3, 1])
b = np.array([0, 2])

c = a + b
d = a - b

print(f'Sum of vectors: {c}')
print(f'Difference of vectors: {d}')
print(f'Multiply: {np.dot(a, b)}')

cos_angle = np.dot(a, b) / la.norm(a) / la.norm(b)
print(f"Косинус кута: {cos_angle}")
print(f"Значення кута (радіани): {np.arccos(cos_angle)}")
print(f"Відстань між векторами: {la.norm(a - b, ord=1)}")
