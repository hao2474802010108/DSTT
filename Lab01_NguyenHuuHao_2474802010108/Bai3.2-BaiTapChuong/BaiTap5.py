#Bài Tập 5

import numpy as np
#1
print("\n1. Khai báo ma trận M1:")
try:
    M1 = np.array([[9, 12], [23, 30]])
    print("Ma trận M1:\n", M1)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#2
print("\n2. Khai báo vector u và thực hiện M1.dot(u):")
try:
    u = np.array([2, 1])
    tichM1u = M1.dot(u)
    print("Vector u:", u)
    print("M1.dot(u) =", tichM1u)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#3
print("\n3. Tính u.dot(M1):")
try:
    tichuM1 = u.dot(M1)
    print("u.dot(M1) =", tichuM1)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#4
print("\n4. Thực hiện np.dot(M1, u):")
try:
    print("np.dot(M1, u) =", np.dot(M1, u))
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#5
print("\n5. Thực hiện np.dot(u, M1):")
try:
    print("np.dot(u, M1) =", np.dot(u, M1))
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
