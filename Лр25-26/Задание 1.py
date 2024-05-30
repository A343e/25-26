import numpy as np

# Создаем одномерный массив
A = np.arange(12, 24)

# Преобразуем его в двумерный
B = A.reshape(3, 4)
print(B)