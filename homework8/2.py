# Задача 2 Измерены значения IQ выборки студентов,
# обучающихся в местных технических вузах:
# 131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
# Известно, что в генеральной совокупности IQ распределен нормально.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.



import numpy as np
from scipy.stats import t

IQ = [131, 125, 115, 122, 131, 115, 107, 99, 125, 111]

mean = np.mean(IQ)
std = np.std(IQ, ddof=1)
n = len(IQ)
confidence = 0.95
alpha = 1 - confidence

# Вычисление доверительного интервала
t_value = t.ppf(1 - alpha / 2, df=n-1)
stderr = std / np.sqrt(n)
lower_bound = mean - t_value * stderr
upper_bound = mean + t_value * stderr

print("Доверительный интервал для математического ожидания (0.95):", lower_bound, upper_bound)