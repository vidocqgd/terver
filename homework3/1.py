# Задача 1. Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. 
# Посчитать (желательно без использования статистических методов наподобие std, var, mean) среднее арифметическое, среднее квадратичное отклонение, смещенную 
# и несмещенную оценки дисперсий для данной выборки.

import math

# Заданная выборка
sample = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]

# Вычисление среднего арифметического
mean = sum(sample) / len(sample)

# Вычисление отклонений каждого элемента от среднего значения
deviations = [(x - mean) for x in sample]

# Вычисление суммы квадратов отклонений
sum_squared_deviations = sum([(x - mean)**2 for x in sample])

# Смещенная оценка дисперсии
variance_biased = sum_squared_deviations / len(sample)

# Несмещенная оценка дисперсии
variance_unbiased = sum_squared_deviations / (len(sample) - 1)

# Вычисление среднего квадратичного отклонения (стандартное отклонение)
standard_deviation = math.sqrt(variance_biased)

# Вывод результатов
print("Среднее арифметическое: ", mean)
print("Смещенная оценка дисперсии: ", variance_biased)
print("Несмещенная оценка дисперсии: ", variance_unbiased)
print("Среднее квадратичное отклонение: ", standard_deviation)