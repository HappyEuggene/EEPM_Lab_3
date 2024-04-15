import numpy as np
from numpy.linalg import eig, inv, matrix_power

# Визначення матриці A
A = np.array([
    [0.4, 0.1, 0.5],
    [0.1, 0.6, 0.3],
    [0.5, 0.3, 0.2]
])

# Розрахунок власних чисел та власних векторів
eigenvalues, eigenvectors = eig(A)

# Коефіцієнти характеристичного поліному
char_poly_coefficients = np.poly(A)

# Число Фробеніуса
frobenius_number = max(abs(eigenvalues))

# Правий та лівий вектори Фробеніуса
right_frobenius_vector = eigenvectors[:, np.argmax(abs(eigenvalues))]
left_frobenius_vector = eig(A.T)[1][:, np.argmax(abs(eig(A.T)[0]))]

# Перевірка, чи є матриця A продуктивною
is_productive = all(abs(eigenvalues) < 1)

# Розрахунок матриці повних витрат B
I = np.identity(3)
B = inv(I - A)

# Сумування ряду E + A + A^2 + ... + A^N до збіжності
sum_series = np.copy(I)
N = 0
while N < 100:
    N += 1
    A_power = matrix_power(A, N)
    sum_series += A_power
    if np.all(np.abs(A_power) < 0.01):
        break

# Розрахунок вектора цін
added_value_vector = np.array([0.4, 0.3, 0.6])
price_vector = added_value_vector.dot(B)

# Вивід результатів
print("Власні числа:", eigenvalues)
print("Коефіцієнти характеристичного поліному:", char_poly_coefficients)
print("Число Фробеніуса:", frobenius_number)
print("Правий вектор Фробеніуса:", right_frobenius_vector)
print("Лівий вектор Фробеніуса:", left_frobenius_vector)
print("Чи є матриця продуктивною:", is_productive)
print("Матриця повних витрат B:", B)
print("Вектор цін:", price_vector)

