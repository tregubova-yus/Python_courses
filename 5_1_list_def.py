#coding=UTF-8

#Задание 5.1

#Оформить функцией поиск в списке

#0 наименование
#1 код товара
#2 рейтинг
#3 цена
#4 мощность подключения
#5 напряжение питания максимальное
#6 количество жил в кабеле подключения
#7 количество уровлней мощности
#8 автоматика закипания
#9 распознание наличия посуды
#10 звуковой сигнал
#11 автоблокировка


#найти максимальное значение в списке
def max_in_list(lst):
	maximum = lst[0]
	for i in range(len(lst)):
		if lst[i] > maximum:
			maximum = lst[i]
	return(maximum)

model = [
['Electrolux_IPE6440KF',1285007,5,34999,7.35,360,4,9,'true','true','true','true'],
['Hansa_BHI68313',1306106,5,20199,7.4,400,0,9,'false','false','true','true'],
['Bosh_PUE611FB1E',1109422,4.5,5199,4.6,230,3,17,'true','true','false','true']
]

print('\nСписок: {0}'.format(model), end = ' ')

new_list = []
for i in range(len(model)):
	new_list.append(model[i][5])

print('\nЗначения напряжений: {0}'.format(new_list))

#найти максимальное напряжение - 5-ый элемент
maximum = max_in_list(new_list)
print('\nЗначение максимального напряжения: {0}'.format(maximum))

