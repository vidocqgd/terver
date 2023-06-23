# Задача 3 Известно, что рост футболистов в сборной распределен нормально
# с дисперсией генеральной совокупности, равной 25 кв.см. Объем выборки равен 27,
# среднее выборочное составляет 174.2. Найдите доверительный интервал для
# математического ожидания с надежностью 0.95.


import numpy as np
from scipy.stats import t

n = 27
mean = 174.2
population_variance = 25
confidence = 0.95
alpha = 1 - confidence

# Вычисление доверительного интервала
t_value = t.ppf(1 - alpha / 2, df=n-1)
stderr = np.sqrt(population_variance / n)
lower_bound = mean - t_value * stderr
upper_bound = mean + t_value * stderr

print("Доверительный интервал для математического ожидания (0.95):", lower_bound, upper_bound)