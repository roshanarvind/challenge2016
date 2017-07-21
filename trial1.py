from sets import Set
import csv

class distributor:
	"""docstring for distributor"""
	dist_total = 0 

	def __init__(self, distributor_id):
		self.distributor_id = distributor_id
		self.i_countries = []
		self.i_provinces = []
		self.i_cities = []
		self.e_countries = []
		self.e_provinces = []
		self.e_cities = []
		dist_total += 1
		

def read_file():
	with open('cities.csv', 'rb') as csvfile:
		return list(csv.reader(csvfile))[1:]

def main():
	cities_list = read_file()
	countries={}
	provinces={}
	cities={}
	a,b,c = 0,0,0
	for row in cities_list:
		if row[5] not in countries:
			a+=1
			countries[row[5]]=a
		if row[4] not in provinces:
			b+=1
			provinces[row[4]]=b
		if row[3] not in cities:
			c+=1	
			cities[row[3]]=c
	
if __name__ == '__main__':
	main()