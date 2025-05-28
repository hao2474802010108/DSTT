# Bài 1.2.1 a - Các phép xử lý với danh sách
# Khởi tạo danh sách
danhsach1 = [1., 3.]
danhsach2 = [5., 7.]
# 1. Phép cộng 2 danh sách (ghép nối)
danhsach = danhsach1 + danhsach2
print("\n1. danhsach1 + danhsach2 =", danhsach) 
# 2. Phép nhân danh sách với số nguyên (lặp lại)
danhsach_gapdoi = 2 * danhsach
print("2. 2 * danhsach =", danhsach_gapdoi)
# 3. Phép nhân danh sách với số nguyên (tương tự)
print("3. danhsach * 2 =", danhsach * 2)
# 4. Phép chia danh sách với số (gây lỗi)
print("\n4. Thử thực hiện danhsach / 2:")
try:
    print(danhsach / 2)
except TypeError as e:
    print("Lỗi:", e)           
    print("Giải thích: Python không hỗ trợ phép chia trực tiếp list với số")
    ket_qua_chia = [x/2 for x in danhsach]
    print("Kết quả khi chia từng phần tử:", ket_qua_chia) 