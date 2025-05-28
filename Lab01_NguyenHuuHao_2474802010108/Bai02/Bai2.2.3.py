# Bài 2.2.3 - Thay thế giá trị trong biểu thức đại số

#1
print("\n1. Import Symbol:")
try:
    from sympy import Symbol
    print("Đã import Symbol từ sympy thành công.")
except ImportError:
    print("Lỗi import Symbol.")
except Exception as e:
    print("Lỗi khác:", type(e).__name__, ":", e)
#2
print("\n2. Khai báo biến x và y:")
try:
    x = Symbol('x')
    y = Symbol('y')
    print("Đã khai báo x và y.")
except Exception as e:
    print("Lỗi khi khai báo biến:", type(e).__name__, ":", e)
#3
print("\n3. Tạo biểu thức bieuthuc = x**2 - x*y + y**2:")
try:
    bieuthuc = x**2 - x*y + y**2
    print("bieuthuc =", bieuthuc)
except Exception as e:
    print("Lỗi khi tạo biểu thức:", type(e).__name__, ":", e)
#4
print("\n4. Thay thế giá trị x=3, y=2 vào biểu thức:")
try:
    giatri = bieuthuc.subs({x: 3, y: 2})
    print("Giá trị của bieuthuc khi x=3, y=2 là:", giatri)
except Exception as e:
    print("Lỗi khi thay thế giá trị:", type(e).__name__, ":", e)
#5
print("\n5. Kiểm tra giá trị của x và y sau khi thay thế:")
try:
    print("Giá trị của x là:", x)
    print("Giá trị của y là:", y)
except Exception as e:
    print("Lỗi khi in giá trị x, y:", type(e).__name__, ":", e)