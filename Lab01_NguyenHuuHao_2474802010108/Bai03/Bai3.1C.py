#Bài 3.1C - Các lệnh xử lý

print("Import numpy")
try:
    import numpy as np
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
# 1
print("\n1. Khai báo vector v = np.array([1., 3., 5.])")
try:
    v = np.array([1., 3., 5.])
    print("v =", v)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#2
print("\n2. Lấy các phần tử vector:")
try:
    print("Danh sách phần tử:", v.tolist())
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#3
print("\n3. v.shape:")
try:
    print("v.shape =", v.shape)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#4
print("\n4. v.transpose():")
try:
    print("v.transpose() =", v.transpose())
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#5
print("\n5. v[1]:")
try:
    print("v[1] =", v[1])
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#6
print("\n6. Thay đổi phần tử v[0] = 5:")
try:
    v[0] = 5
    print("v sau khi thay đổi:", v)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#7
print("\n7. v[1:2]:")
try:
    print("v[1:2] =", v[1:2])
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#8
print("\n8. Gán v[1:2] = [1., 2.]")
try:
    v[1:2] = [1., 2.]
    print("v sau khi gán:", v)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)

#9
print("\n9. Tính v3 = 2 * v[2] + v[1] * 3")
try:
    v3 = 2 * v[2] + v[1] * 3
    print("v3 =", v3)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#10
print("\n10. Gán v1 = [4., 6.]")
try:
    v1 = np.array([4., 6.])
    print("v1 =", v1)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#11
print("\n11. Tính v + v1:")
try:
    print("v + v1 =", v + v1)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#12
print("\n12. Một số phép toán trên vector:")
try:
    x = np.array([1, 10, 100])
    print("x =", x)
    print("np.sqrt(x) =", np.sqrt(x))
    print("np.log10(x) =", np.log10(x))
    print("np.exp(x) =", np.exp(x))
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#13
print("\n13. Tích vô hướng: np.dot([1,2,3], [4,5,6])")
try:
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print("np.dot(a, b) =", np.dot(a, b))
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)