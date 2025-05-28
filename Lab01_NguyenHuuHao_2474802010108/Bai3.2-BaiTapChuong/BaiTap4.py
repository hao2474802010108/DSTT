#Bài Tập 4
#1
print("\n1. Khai báo biến và phương trình:")
try:
    from sympy import Symbol, solve
    x = Symbol('x')
    y = Symbol('y')
    pt1 = 2*x + 3*y - 12
    pt2 = 3*x - 2*y - 5
    print("Phương trình 1:", pt1)
    print("Phương trình 2:", pt2)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#2
print("\n2. Giải hệ phương trình:")
try:
    nghiem = solve((pt1, pt2), dict=True)
    print("Nghiệm của hệ phương trình là:", nghiem)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#3
print("\n3. Kiểm tra nghiệm:")
try:
    if nghiem:
        n0 = nghiem[0]
        ktra1 = pt1.subs({x: n0[x], y: n0[y]})
        ktra2 = pt2.subs({x: n0[x], y: n0[y]})
        print("Thay vào phương trình 1 được:", ktra1)
        print("Thay vào phương trình 2 được:", ktra2)
    else:
        print("Không có nghiệm để kiểm tra.")
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)