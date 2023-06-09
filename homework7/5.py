# Задача 5. Заявляется, что партия изготавливается со средним арифметическим 2,5 см. Проверить
# данную гипотезу, если известно, что размеры изделий подчинены нормальному закону
# распределения. Объем выборки 10, уровень статистической значимости 5%
# 2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34

import math

samples = [2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34]
population_mean = 2.5
alpha = 0.05
n = len(samples)

sample_mean = sum(samples) / n
sample_std = math.sqrt(sum((x - sample_mean) ** 2 for x in samples) / (n - 1))
standard_error = sample_std / math.sqrt(n)
t_statistic = (sample_mean - population_mean) / standard_error

# Для уровня статистической значимости 0.05 и n-1 степеней свободы, критическое значение t-статистики равно 2.262
critical_value = 2.262

if abs(t_statistic) > critical_value:
    print("Среднее арифметическое отличается от заявленного значения.")
else:
    print("Среднее арифметическое не отличается от заявленного значения.")