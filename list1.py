#Список

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

model = [
['Electrolux_IPE6440KF',1285007,5,34999,7.35,360,4,9,'true','true','true','true'],
['Hansa_BHI68313',1306106,5,20199,7.4,400,0,9,'false','false','true','true'],
['Bosh_PUE611FB1E',1109422,4.5,5199,4.6,230,3,17,'true','true','false','true']
]

#найти максимальное напряжение - 5-ый элемент
maximum = model[0][5]
for i in range(len(model)):
	if model[i][5] > maximum:
		maximum = model[i][5]
print(maximum)


