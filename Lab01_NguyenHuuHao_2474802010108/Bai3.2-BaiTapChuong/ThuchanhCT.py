#Bài tập thực hiện các phép tinh rồi in ra -Bài tập về nhà
import numpy as np

# Câu hỏi: Cho biết mat1?
mat1 = np.zeros((5,5))
print("mat1 =\n", mat1)

# Câu hỏi: Cho biết mat2?
mat2 = np.ones((5,5))
print("\nmat2 =\n", mat2)

# Câu hỏi: Cho biết mat3?
mat3 = mat1 + 2 * mat2
print("\nmat3 =\n", mat3)

# Câu hỏi: Cho biết mat3 và mat4? (mat3 thay đổi thì mat4 có thay đổi theo không?)
mat4 = mat3
mat3[3][2] =10
print("\nSau khi gán mat4 = mat3 và thay đổi mat3[3][2] = 10:")
print("mat3 =\n",mat3)
print("mat4 =\n",mat4)
print("Vì mat4 = mat3 là gán tham chiếu nên cả hai cùng thay đổi.")

# Câu hỏi: Cho biết mat3, mat4 và mat5? (mat3 thay đổi thì mat4 và mat5 có thay đổi theo không?)
mat5 = np.copy(mat3)
mat3[3][1] =10
print("\nSau khi copy và thay đổi mat3[3][1] = 10:")
print("mat3 =\n",mat3)
print("mat4 =\n",mat4)
print("mat5 =\n",mat5)
print("Vì mat5 là bản sao nên không bị thay đổi.")

# Câu hỏi: hãy cho biết mat6?
mat6 = np.empty((4,5))
print("\nmat6 =\n",mat6)
print("mat6 chứa giá trị rác (không xác định).")

# Câu hỏi: hãy cho biết mat7?
mat7 = np.identity(4)
print("\nmat7 =\n",mat7)

# Câu hỏi: hãy cho biết mat8?
mat8 = np.random.rand(4,5)
print("\nmat8 =\n",mat8)