#coding=UTF-8
"""
Задание 6.1
Описать классом данные
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

electrilux = Characteristics('id1','Electrolux_IPE6440KF',1285007,5,34999,7.35,360,4,9)
hansa = Characteristics('id2','Hansa_BHI68313',1306106,5,20199,7.4,400,0,9)
bosh = Characteristics('id3','Bosh_PUE611FB1E',1109422,4.5,35199,4.6,230,3,17)
model = {
	electrilux.key:electrilux,
	hansa.key:hansa,
	bosh.key:bosh,
}

#pprint (model)
pprint (model[hansa.key])


"""
model_old = {
	'Electrolux_IPE6440KF':
	{'код товара':1285007,
	'рейтинг':5,
	'цена':34999,
	'мощность подключения':7.35,
	'напряжение питания':360,
	'количество жил в кабеле подключения':4,
	'количество уровней мощности':9
	},

	'Hansa_BHI68313':
	{'код товара':1306106,
	'рейтинг':5,
	'цена':20199,
	'мощность подключения':7.4,
	'напряжение питания':400,
	'количество жил в кабеле подключения':0,
	'количество уровней мощности':9
	},

	'Bosh_PUE611FB1E':
	{'код товара':1109422,
	'рейтинг':4.5,
	'цена':35199,
	'мощность подключения':4.6,
	'напряжение питания':230,
	'количество жил в кабеле подключения':3,
	'количество уровней мощности':17
	}
	}

pprint(model_old)
"""


