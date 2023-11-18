# Програмування таблиці істинності
X_arr=[False,True,False,True]
Y_arr=[False,False,True,True]
print("#| X | Y | X∧Y | X∨Y |")
for i in range(len(X_arr)):
    print(f"{i+1}|{X_arr[i]}|{Y_arr[i]}|{X_arr[i] and Y_arr[i]}|{X_arr[i] or Y_arr[i]}|")

# # | X | Y | X∧Y | X∨Y |
# 1|False|False|False|False|
# 2|True|False|False|True|
# 3|False|True|False|True|
# 4|True|True|True|True|