# Bài 6 - Tìm chỗ đóng quân an toàn

import numpy as np
#1
print("\n1. Khởi tạo dữ liệu nguy cơ từ các nhóm:")
try:
    A = np.array([[1,1,0,0,1], [3,1,0,1,1], [5,2,0,1,2], [2,0,1,2,3]])
    B = np.array([[1,1,2,2,1], [2,2,2,0,2], [0,1,2,4,2], [1, 4, 1, 2, 2]])
    C = np.array([[0, 5, 1, 1, 1], [0, 1, 1, 1, 3], [1, 3, 1, 3, 1], [0, 1, 3, 3, 0]])
    D = np.array([[3, 1, 1, 0, 1], [5, 0, 0, 3, 7], [7, 0, 0, 3, 5], [5, 0, 3, 5, 3])
    E = np.array([[0,0,0,10,0], [0, 0,15, 0, 0], [0, 5,15, 5, 0], [0,20, 5, 0, 0]])
    print("Dữ liệu nguy cơ đã khởi tạo thành công.")
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#2
def find_safe_positions(mats, threshold=5):
    try:
        total_risk = sum(mats)
        safe_pos = np.argwhere(total_risk <= threshold)
        return safe_pos
    except Exception as e:
        print("Lỗi trong hàm find_safe_positions:", type(e).__name__, ":", e)
        return []
#3
print("\n2. Kiểm tra các kịch bản đóng quân:")
#a
print("\na) Đóng quân ngắn hạn (1-2 ngày) - chỉ tránh lộ bí mật:")
try:
    safe_a = find_safe_positions([E])
    print("Các vị trí an toàn:", safe_a)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#b
print("\nb) Huấn luyện - tránh lộ bí mật và bệnh dịch:")
try:
    safe_b = find_safe_positions([D, E])
    print("Các vị trí an toàn:", safe_b)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#c
print("\nc) Mùa khô - tránh cháy rừng, lộ bí mật, sạt lở núi:")
try:
    safe_c = find_safe_positions([A, C, E])
    print("Các vị trí an toàn:", safe_c)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#d
print("\nd) Mùa mưa - tránh lũ, sạt lở và bệnh dịch:")
try:
    safe_d = find_safe_positions([B, C, D])
    print("Các vị trí an toàn:", safe_d)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#e
print("\ne) An toàn toàn diện trong 8 tháng:")
try:
    safe_e = find_safe_positions([A, B, C, D, E])
    print("Các vị trí an toàn:", safe_e)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
