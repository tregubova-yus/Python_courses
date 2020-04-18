#coding=UTF-8

#Задание 5.2

#Оформить функцией поиск в словаре

#найти минимальное значение
def min_in_list(lst,k):
	minimum = lst[0][k]
	for i in range(len(lst)):
		if lst[i][k] < minimum:
			minimum = lst[i][k]
	return(minimum)

model = {
	'Electrolux_IPE6440KF':34999,
	'Hansa_BHI68313':20199,
	'Bosh_PUE611FB1E':35199
	}

list_d = list(model.items())

print('\nЗначения: {0}'.format(model))

minimum = min_in_list(list_d,1)
print('\nЗначение наименьшей цены: {0}'.format(minimum))