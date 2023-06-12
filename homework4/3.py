# Задача 3. Непрерывная случайная величина X распределена нормально и задана плотностью
# распределения f(x) = (1 / (4 * sqrt(2pi))) * exp((-(x+2)**2) / 32)
# Найдите: а). M(X) б). D(X) в). std(X) (среднее квадратичное отклонение)

import math

# Функция для вычисления значения плотности нормального распределения
def normal_density(x):
    return (1 / (4 * math.sqrt(2*math.pi))) * math.exp(-((x+2)**2) / 32)

# Вычисление математического ожидания (M(X))
mean = 0
for x in range(-100, 101):
    mean += x * normal_density(x)
    
# Вычисление дисперсии (D(X))
variance = 0
for x in range(-100, 101):
    variance += ((x - mean) ** 2) * normal_density(x)
    
# Вычисление среднего квадратического отклонения (std(X))
std_deviation = math.sqrt(variance)

print("M(X):", mean)
print("D(X):", variance)
print("std(X):", std_deviation)
