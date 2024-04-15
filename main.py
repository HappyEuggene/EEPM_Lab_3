import numpy as np
import matplotlib.pyplot as plt

# Вихідні дані з задачі
output_industry = 2000  # млн грн
output_agriculture = 1250  # млн грн

# Вектор внутрішніх витрат (вихідних потоків в інші галузі)
industry_to_self = 800
industry_to_agri = 400
agri_to_industry = 300
agri_to_self = 350

# Внутрішні та кінцеві споживачі
consumer_industry = 800
consumer_agriculture = 600

# Коефіцієнти технічних витрат
a11 = industry_to_self / output_industry
a12 = agri_to_industry / output_agriculture
a21 = industry_to_agri / output_industry
a22 = agri_to_self / output_agriculture

# Матриця технічних коефіцієнтів A
A = np.array([[a11, a12], [a21, a22]])

# Вектор кінцевого попиту з урахуванням прогнозованого зростання
final_demand = np.array([1100, 850])  # млн грн

# Обчислення повного випуску за формулою X = (I - A)^-1 * D
I = np.identity(2)
X = np.linalg.inv(I - A).dot(final_demand)

# Labels and data preparation for the first plot
categories = ['Потреби промисловості', 'Потреби сіль.гос.', 'Споживання населення']
industry_data = [industry_to_self, industry_to_agri, consumer_industry]
agriculture_data = [agri_to_industry, agri_to_self, consumer_agriculture]

x = np.arange(len(categories))  # мітки на осі X
width = 0.35  # ширина стовпців

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, industry_data, width, label='Промисловість')
rects2 = ax.bar(x + width/2, agriculture_data, width, label='Сільське господарство')

ax.set_ylabel('Млн грн')
ax.set_title('Розподіл виробничих потреб і споживання за минулий рік')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()

# Labels for the second plot
sector_labels = ['Промисловість', 'Сільське господарство']

# Plot for projected full production
fig, ax2 = plt.subplots()
ax2.bar(sector_labels[0], X[0], color='yellow')
ax2.bar(sector_labels[1], X[1], color='blue')
ax2.set_ylabel('Млн грн')
ax2.set_title('Прогнозований повний випуск на наступний рік')

plt.show()
