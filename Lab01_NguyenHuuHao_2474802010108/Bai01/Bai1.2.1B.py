# Bài 1.2.1 B  - Ghép các danh sách bằng lệnh zip:
mon_hoc = ["ToanCC", "DSTT", "ToanRR", "LaptrinkCB"]
thu_tu = [2, 3, 4, 1]
diem_so = [10, 9, 8, 7]
try:
    anh_xa = list(zip(thu_tu, mon_hoc, diem_so))
    print("\n1. Kết quả zip():", anh_xa)
    tap_hop = set(anh_xa)
    print("2. Kết quả set():", tap_hop)
    lay_TT, lay_monhoc, lay_diem = zip(*anh_xa)
    print("3. Kết quả phân rã:")
    print("Thứ tự môn:", lay_TT)
    print("Tên môn học:", lay_monhoc)
    print("Điểm số:", lay_diem)
except TypeError as e:
    print("Lỗi xảy ra:", e)
    print("Kiểm tra lại độ dài các list đầu vào")
except Exception as e:
    print("Lỗi không xác định:", type(e).__name__, ":", e)