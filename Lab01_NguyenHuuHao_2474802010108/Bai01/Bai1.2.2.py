#Bài 1.2.2 - Lệnh thực thi một tập tin python
#1
print("\n1. Thao tác với list:")
try:
    mylist = [100, 200, 300]
    print("mylist =", mylist)
    a = b = c = 0
    print("a, b, c =", a, b, c) 
    mylist_empty = []
    print("mylist_empty =", mylist_empty) 
except Exception as e:
    print("Lỗi:", type(e).__name__, ":", e)
#2
print("\n2. Import module:")
try:
    print("Giả định import từ file fluctial1.py")
    print("Đã import module (giả định)")
except ImportError:
    print("Không tìm thấy file module!")
except Exception as e:
    print("Lỗi khác:", e)
