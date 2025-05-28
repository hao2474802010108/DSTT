# Bài 1.2.1 C  - Xây dựng danh sách:
print("\n1. Kết quả itertools.chain():")
import itertools
try:
    tap_sinh = list(itertools.chain(range(4), range(5,10), range(15,20)))
    print("tap_sinh =", tap_sinh)
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
print("\n2. Kết quả zip() với reversed():")
try:
    ket_qua = list(zip(range(4), range(7, 12), reversed(range(11))))
    print("Kết quả =", ket_qua)
except SyntaxError:
    print("Phát hiện lỗi SyntaxError: Dấu ngoặc không cân bằng trong đề bài")
    print("→ Đang sửa lại thành cú pháp đúng...")
    ket_qua = list(zip(range(4), range(7, 12), reversed(range(11))))
    print("Kết quả sau khi sửa =", ket_qua) 
except Exception as e:
    print("Lỗi khác:", type(e).__name__, ":", e)