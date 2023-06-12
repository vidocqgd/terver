# На сколько сигм (средних квадратичных отклонений) отклоняется рост человека, равный 190 см, от
# математического ожидания роста в популяции, в которой M(X) = 178 см и D(X) = 25 кв.см?

import math

def calculate_sigma(x, mean, variance):
    std_dev = math.sqrt(variance)
    z = (x - mean) / std_dev
    return z

height = 190
mean = 178
variance = 25

sigma = calculate_sigma(height, mean, variance)
print("Количество сигм отклонения:", sigma)