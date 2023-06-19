# Задача 1. Известно, что генеральная совокупность распределена нормально
# со средним квадратическим отклонением, равным 16.
# Найти доверительный интервал для оценки математического ожидания с надежностью 0.95,
# если выборочная средняя M = 80, а объем выборки n = 256.


import scipy.stats as stats

# Исходные данные
std_dev = 16
sample_mean = 80
sample_size = 256
confidence = 0.95

# Вычисление стандартной ошибки
standard_error = std_dev / (sample_size ** 0.5)

# Вычисление доверительного интервала
margin_of_error = stats.norm.ppf((1 + confidence) / 2) * standard_error
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)

# Вывод результата
print(f"Доверительный интервал: {confidence_interval}")