#Bài 2.1 - Làm quen với Symbol trong SymPy

#1
from sympy import Symbol, symbols, expand
x = Symbol('x')
y = Symbol('y')
print("Symbol x:", x)
print("Symbol y:", y)
#2
print("\n2. PHÉP TOÁN HÌNH THỨC")
expr1 = x + x + x + 2
print("x + x + x + 2 =", expr1)  # Kết quả: 3*x + 2
expr2 = x*y + y*x
print("x*y + y*x =", expr2)  # Kết quả: 2*x*y
#3
print("\n3. BIỂU THỨC PHỨC TẠP VÀ LỆNH EXPAND")
p = (x+2)*(y+3)
print("(x+2)(y+3) (chưa khai triển):", p)
p_expanded = expand(p)
print("Sau khi expand:", p_expanded) 
#4
print("\n4. VÍ DỤ VỚI TÊN SYMBOL ĐẶC BIỆT")
try:
    no = Symbol('No?')
    chim = Symbol('Chim?')
    expr3 = 3*chim+7*no
    print("3*Chim?+7*No? =", expr3)
    print("\n Tên các symbol:")
    print("no.name=", no.name)
    print("chim.name=", chim.name)
except Exception as e:
    print("Lỗi:", e)
#5
print("\n5. TỰ ĐỘNG ĐƠN GIẢN HÓA")
expr4 = x*(x+2*x-x)
print("x*(x+2x-x) =", expr4)