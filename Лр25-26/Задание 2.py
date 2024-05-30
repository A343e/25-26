import numpy as np

# Создаем массив из случайных чисел
C = np.random.normal(0, 1, (3, 4))

# Преобразуем его в одномерный
D = C.flatten()
print(D)