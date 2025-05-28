#Bài tập 1
print("\n=== GIẢI PHƯƠNG TRÌNH VỚI SYMPY ===\n")

from sympy import Symbol, solve
#1
print("1. PHƯƠNG TRÌNH BẬC 1:")
x = Symbol('x')
bicuthuc1=x+3-5
nghiem1=solve(bicuthuc1)
print(f"Phương trình x + 3 - 5 = 0 có nghiệm: {nghiem1}")
print(f"Truy xuất nghiệm đầu tiên: nghiem1[0] = {nghiem1[0]}\n")
#2
print("2. PHƯƠNG TRÌNH BẬC 2:")
bicuthuc2=x**2+3-5
nghiem2=solve(bicuthuc2)
print(f"Phương trình x² + 3 - 5 = 0 có nghiệm: {nghiem2}")
print(f"Nghiệm thứ nhất: nghiem2[0] = {nghiem2[0]}")
print(f"Nghiệm thứ hai: nghiem2[1] = {nghiem2[1]}")