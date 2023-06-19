# Задача 3. Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
# Рост матерей 178, 165, 165, 173, 168, 155, 160, 164, 178, 175
# Используя эти данные построить 95% доверительный интервал для разности среднего
# роста родителей и детей


import numpy as np
from scipy.stats import t

# Рост дочерей и матерей
daughters_height = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
mothers_height = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])

# Вычисление средних значений роста дочерей и матерей
mean_daughters = np.mean(daughters_height)
mean_mothers = np.mean(mothers_height)

# Вычисление стандартных отклонений роста дочерей и матерей
std_daughters = np.std(daughters_height, ddof=1)
std_mothers = np.std(mothers_height, ddof=1)

# Вычисление стандартной ошибки разности средних
n1 = len(daughters_height)
n2 = len(mothers_height)
se = np.sqrt((std_daughters**2 / n1) + (std_mothers**2 / n2))

# Вычисление доверительного интервала
df = n1 + n2 - 2
confidence_interval = t.interval(0.95, df, loc=(mean_daughters - mean_mothers), scale=se)

# Вывод результатов
print("Доверительный интервал для разности среднего роста матерей и дочерей:")
print("Нижняя граница:", confidence_interval[0])
print("Верхняя граница:", confidence_interval[1])