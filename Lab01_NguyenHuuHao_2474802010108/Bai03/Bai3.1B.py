#Bài 3.1 B Lưu ý - Trong numpy

print("\n0. Import numpy")
try:
    import numpy as np
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#1
print("\n1. Truy xuất phần tử thứ 3 của vec3 (vec3[2]):")
try:
    vec3 = np.array([2., 4., 6.])
    print("vec3[2]:", vec3[2])
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#2
print("\n2. Tạo vec4 = np.linspace(0, 20, 5):")
try:
    vec4 = np.linspace(0, 20, 5)
    print("vec4:", vec4)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)

#3
print("\n3. Tạo vec5 = np.zeros(5):")
try:
    vec5 = np.zeros(5)
    print("vec5:", vec5)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#4
print("\n4. Tạo vec6 = np.ones(5):")
try:
    vec6 = np.ones(5)
    print("vec6:", vec6)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#5
print("\n5. Tạo vec7 = np.empty(5):")
try:
    vec7 = np.empty(5)
    print("vec7 (có thể là giá trị rác):", vec7)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#6
print("\n6. Tạo vector ngẫu nhiên: np.random.rand(5)")
try:
    vec_random = np.random.rand(5)
    print("vec_random:", vec_random)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
print("\n6b. Hoặc dùng np.random.random(5):")
try:
    vec_random2 = np.random.random(5)
    print("vec_random2:", vec_random2)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)