# Bài 2.2.1 - Đặt nhân tử chung và khai triển biểu thức

# 1
print("\n1. Import Symbol, factor, expand:")
try:
    from sympy import Symbol, factor, expand
    print("Đã import thành công các hàm từ sympy.")
except ImportError:
    print("Không thể import các hàm từ sympy.")
except Exception as e:
    print("Lỗi khác:", type(e).__name__, ":", e)
# 2
print("\n2. Khai báo biểu thức x**3 - y**3:")
try:
    x=Symbol('x')
    y=Symbol('y')
    bieuthuc = x**3 - y**3
    print("Biểu thức khai triển bieuthuc =", bieuthuc)
except Exception as e:
    print("Lỗi khi khai báo biểu thức:", type(e).__name__, ":", e)
# 3
print("\n3. Sử dụng factor để đưa về tích:")
try:
    ket_qua_factor = factor(bieuthuc)
    print("Kết quả factor(bieuthuc) =", ket_qua_factor)
except Exception as e:
    print("Lỗi khi dùng factor:", type(e).__name__, ":", e)
# 4
print("\n4. Sử dụng expand để khai triển biểu thức tích:")
try:
    bieuthuc_tich = (x - y)*(x**2 + x*y + y**2)
    ket_qua_expand = expand(bieuthuc_tich)
    print("Kết quả expand(bieuthuc_tich) =", ket_qua_expand)
except Exception as e:
    print("Lỗi khi dùng expand:", type(e).__name__, ":", e)