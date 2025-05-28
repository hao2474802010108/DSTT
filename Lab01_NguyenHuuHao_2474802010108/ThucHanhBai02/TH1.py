# Bài 2.2.3 - Thay thế giá trị trong biểu thức đại số bằng SymPy

#1
print("\n1. Khởi tạo biểu thức:")
try:
    from sympy import Symbol
    x = Symbol('x')
    y = Symbol('y')
    bieuthuc = x**2 - x*y + y**2
    print("Biểu thức: ", bieuthuc)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#2 Tạo các tình huống
#Tình huống 1: Thay x = 3, y = x
print("\n2. Tình huống 1: Thay x = 3, y = x")
try:
    giatri = bieuthuc.subs({x: 3, y: x})
    print("Giá trị:", giatri)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)

#Tình huống 2: Thay x = y, y = 3
print("\n3. Tình huống 2: Thay x = y, y = 3")
try:
    giatri = bieuthuc.subs({x: y, y: 3})
    print("Giá trị:", giatri)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)

#Tình huống 3: Thay y = x rồi x = 3
print("\n4. Tình huống 3: Thay y = x rồi x = 3")
try:
    giatri = bieuthuc.subs({y: x}).subs({x: 3})
    print("Giá trị:", giatri)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#3
print("\n5. Rút gọn biểu thức sau khi thay x = 1 - y")
try:
    bieuthuc_moi = bieuthuc.subs({x: 1 - y})
    print("Biểu thức sau thay: ", bieuthuc_moi)
    from sympy import simplify
    dongian = simplify(bieuthuc_moi)
    print("Biểu thức rút gọn: ", dongian)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)