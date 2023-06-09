# Задачу 4 решать с помощью функции.
# Задача 4. Есть ли статистически значимые различия в среднем росте матерей и дочерей?
# Рост матерей 172, 177, 158, 170, 178,175, 164, 160, 169, 165
# Рост взрослых дочерей: 173, 175, 162, 174, 175, 168, 155, 170, 160, 163


from scipy.stats import ttest_ind

# Рост матерей
mothers_height = [172, 177, 158, 170, 178, 175, 164, 160, 169, 165]

# Рост дочерей
daughters_height = [173, 175, 162, 174, 175, 168, 155, 170, 160, 163]

# Проведение t-теста
t_statistic, p_value = ttest_ind(mothers_height, daughters_height)

# Уровень значимости
alpha = 0.05

# Проверка гипотезы
if p_value < alpha:
    result = "Есть статистически значимые различия"
else:
    result = "Нет статистически значимых различий"

# Вывод результатов
print(result)