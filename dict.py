#coding=UTF-8

#Задание 3.2

#Словарь

model = {
	'Electrolux_IPE6440KF':34999,
	'Hansa_BHI68313':20199,
	'Bosh_PUE611FB1E':35199
	}

list_d = list(model.items())

#найти наименьшую цену
minimum = list_d[0][1]
for i in range(len(list_d)):
	if list_d[i][1] < minimum:
		minimum = list_d[i][1]
print(minimum)

