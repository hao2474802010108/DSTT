# Bài 3.1 - Một số lệnh cơ bản NumPy xử lý vector

print("\n0. Khởi tạo thư viện numpy:")
try:
    import numpy as np
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)

#1 Khởi tạo vec1
print("\n1. Khởi tạo vec1 = np.array([1., 3., 5.])")
try:
    vec1 = np.array([1., 3., 5.])
    print("vec1:", vec1)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)

#2 Nhân vec1 với 2
print("\n2. vec1 * 2:")
try:
    print(vec1 * 2)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)

#3 Nhân vec1 * vec1
print("\n3. vec1 * vec1 (phép nhân từng phần tử - broadcasting):")
try:
    print(vec1 * vec1)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)

#4 Chia vec1 / 2
print("\n4. vec1 / 2:")
try:
    print(vec1 / 2)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)

#5 Cộng vec1 + vec1
print("\n5. vec1 + vec1:")
try:
    print(vec1 + vec1)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)

#6 Khởi tạo vec2 và thử cộng với vec1
print("\n6. vec2 = np.array([2., 4.]) và vec1 + vec2:")
try:
    vec2 = np.array([2., 4.])
    print("vec1 + vec2:", vec1 + vec2)
except Exception as e:
    print("Lỗi (vec1 và vec2 khác kích thước):", type(e).__name__, ":", e)

#7 Khởi tạo vec3 = [2., 4., 6.] và cộng với vec1
print("\n7. vec3 = np.array([2., 4., 6.]) và vec1 + vec3:")
try:
    vec3 = np.array([2., 4., 6.])
    print("vec1 + vec3:", vec1 + vec3)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)

#8 Chia vec1 / vec3
print("\n8. vec1 / vec3:")
try:
    print(vec1 / vec3)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)

#9 Nhân vec1 * vec3
print("\n9. vec1 * vec3:")
try:
    print(vec1 * vec3)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)

#10 Tổ hợp 2*vec1 + 5*vec3
print("\n10. 2 * vec1 + 5 * vec3:")
try:
    print(2 * vec1 + 5 * vec3)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)