#Bài tập 3

#1
print("\n1. Khai báo biến và phương trình:")
try:
    from sympy import Symbol, solve
    x = Symbol('x')
    a = Symbol('a')
    b = Symbol('b')
    c = Symbol('c')
    ptb2 = a*x**2 + b*x + c
    print("Phương trình bậc 2:", ptb2)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#2
print("\n2. Giải phương trình theo ẩn x:")
try:
    nghiem = solve(ptb2, x, dict=True)
    print("Nghiệm của phương trình là:", nghiem)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)