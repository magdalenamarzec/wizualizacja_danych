import matplotlib.pyplot as plt

print("\n\nWyświetlenie pojedycznego punktu")

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

#Zdefiniowanie tytułu wykresu i etykiet osi
ax.set_title("Kwadraty liczb", fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

#Zdefiniowanie wielkości etykiet
ax.tick_params(axis='both', labelsize=14)

plt.show()

print("\n\nWyświetlenie serii punktów")
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

#Zdefiniowanie tytułu wykresu i etykiet osi
ax.set_title("Kwadraty liczb", fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

#Zdefiniowanie wielkości etykiet
ax.tick_params(axis='both', labelsize=14)

plt.show()


print("\n\nAutomatyczne obliczanie danych")
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c='yellow', s=10) #c-kolor, s-szerokość linii

#Zdefiniowanie tytułu wykresu i etykiet osi
ax.set_title("Kwadraty liczb", fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

#Zdefiniowanie zakresu dla każdej z osi.
ax.axis([0, 1_100, 0, 1_100_000])
plt.show()


print("\n\nZastosowanie mapy kolorów")
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10) #c-kolor, s-szerokość linii


plt.savefig('squares_plot.png', bbox_inches='tight')


