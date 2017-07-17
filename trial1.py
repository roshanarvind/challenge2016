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
	countries=Set([])
	provinces=Set([])
	cities=Set([])
	for row in cities_list:
		countries.add(row[5])
		provinces.add(row[4])
		cities.add(row[3])
	print len(cities), len(provinces), len(countries)
	print countries

if __name__ == '__main__':
	main()