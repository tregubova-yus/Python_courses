#coding=UTF-8
"""
Задание 6.2
Поиск в словаре
"""
from pprint import pprint

class Characteristics:
	def __init__(self,idn,name,code,rating,price,power,voltage,cable,levels):
		"""Constructor. Attrubutes"""
		self.idn = idn
		self.name = name
		self.code = code
		self.rating = rating
		self.price = price
		self.power = power
		self.voltage = voltage
		self.cable = cable
		self.levels = levels
		self.key = (name)
	
	def __repr__(self):
		return "'%s',%s, %s, %s" % (self.name,self.code, self.rating, self.price)

	def __eq__(self,obj):
		if type(obj) == str:
			return obj in [self.name, self.code, self.rating, self.price]

q = str(input("Введите значение для поиска: "))
#q = 'Electrolux_IPE6440KF'
flag = True

electrolux = Characteristics('id1','Electrolux_IPE6440KF',1285007,5,34999,7.35,360,4,9)
hansa = Characteristics('id2','Hansa_BHI68313',1306106,5,20199,7.4,400,0,9)
bosh = Characteristics('id3','Bosh_PUE611FB1E',1109422,4.5,35199,4.6,230,3,17)

model = {
	electrolux.key:electrolux,
	hansa.key:hansa,
	bosh.key:bosh,
}

for Characteristics in model.values():
	if Characteristics == q:
		print(Characteristics)
		flag = False

if flag:
    print('Нет такого значения')
