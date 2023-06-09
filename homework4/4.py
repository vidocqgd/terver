# Задача 4. Рост взрослого населения города X имеет нормальное распределение, причем, средний рост равен 174 см, а среднее квадратическое отклонение равно 8 см. посчитайте, какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
# 1. больше 182 см?
# 2. больше 190 см?
# 3. от 166 см до 190 см?
# 4. от 166 см до 182 см?
# 5. от 158 см до 190 см?
# 6. не выше 150 см или не ниже 190 см?
# 7. не выше 150 см или не ниже 198 см?
# 8. ниже 166 см?


import math

# Функция для вычисления значения функции плотности стандартного нормального распределения
def standard_normal_density(x):
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * x**2)

# Функция для вычисления значения функции распределения стандартного нормального распределения
def standard_normal_cdf(x):
    return (1 + math.erf(x / math.sqrt(2))) / 2

# Функция для вычисления вероятности, используя стандартное нормальное распределение
def normal_probability(x, mean, std_dev):
    z = (x - mean) / std_dev
    return 1 - standard_normal_cdf(z)

# Заданные параметры
mean = 174
std_dev = 8

# Вычисление вероятности для различных случаев

# Вероятность, что рост больше 182 см
p1 = 1 - standard_normal_cdf((182 - mean) / std_dev)

# Вероятность, что рост больше 190 см
p2 = 1 - standard_normal_cdf((190 - mean) / std_dev)

# Вероятность, что рост находится в диапазоне от 166 см до 190 см
p3 = standard_normal_cdf((190 - mean) / std_dev) - standard_normal_cdf((166 - mean) / std_dev)

# Вероятность, что рост находится в диапазоне от 166 см до 182 см
p4 = standard_normal_cdf((182 - mean) / std_dev) - standard_normal_cdf((166 - mean) / std_dev)

# Вероятность, что рост находится в диапазоне от 158 см до 190 см
p5 = standard_normal_cdf((190 - mean) / std_dev) - standard_normal_cdf((158 - mean) / std_dev)

# Вероятность, что рост не выше 150 см или не ниже 190 см
p6 = standard_normal_cdf((150 - mean) / std_dev) + 1 - standard_normal_cdf((190 - mean) / std_dev)

# Вероятность, что рост не выше 150 см или не ниже 198 см
p7 = standard_normal_cdf((150 - mean) / std_dev) + 1 - standard_normal_cdf((198 - mean) / std_dev)

# Вероятность, что рост ниже 166 см
p8 = standard_normal_cdf((166 - mean) / std_dev)

# Вывод результатов
print("Вероятность, что рост больше 182 см:", p1)
print("Вероятность, что рост больше 190 см:", p2)
print("Вероятность, что рост от 166 см до 190 см:", p3)
print("Вероятность, что рост от 166 см до 182 см:", p4)
print("Вероятность, что рост от 158 см до 190 см:", p5)
print("Вероятность, что рост не выше 150 см или не ниже 190 см:", p6)
print("Вероятность, что рост не выше 150 см или не ниже 198 см:", p7)
print("Вероятность, что рост ниже 166 см:", p8)