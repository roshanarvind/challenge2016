import re
import csv

class distributor:
	"""docstring for distributor"""
	dist_total = 0 

	def __init__(self, distributor_id, include, exclude):
		self.distributor_id = distributor_id
		self.include = include
		self.exclude = exclude
		dist_total += 1
		

def read_file():
	with open('cities.csv', 'rb') as csvfile:
		return list(csv.reader(csvfile))[1:]

def main():
	cities_list = read_file()
	print cities_list

if __name__ == '__main__':
	main()