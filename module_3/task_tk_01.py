import tk_coord
import numpy as np

A = np.array([[2, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

C = A.dot(B)


#  задамо один одиничний вектор
if __name__ == "__main__":

    # tk_coord.vector(0, 0, 1, 1)
    # tk_coord.root.mainloop()

    print(C)
