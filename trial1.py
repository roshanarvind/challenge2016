import csv

distributor_list=[]
dist_total=0
def counter():
	dist_total+=1
	return dist_total

countries={}
provinces={}
cities={}
class distributor:
	"""docstring for distributor"""
	dist_total = 1
	def __init__(self,co_list_i,ci_list_i,pr_list_i,co_list_e,ci_list_e,pr_list_e):
		self.distributor_id = counter()
		self.i_countries = co_list_i
		self.i_provinces = pr_list_i
		self.i_cities = ci_list_i
		self.e_countries = co_list_e
		self.e_provinces = pr_list_e
		self.e_cities = ci_list_e

	def add_parent_link(self, parent_id):
		#self.i_countries.append()
		i=0

def search(string, id):
	if id==1:
		if string in cities:
			return cities[string]
	if id==2:
		if string in provinces:
			return provinces[string]
	if id==3:
		if string in countries:
			return countries[string]
	return -1 
def add_distributor():
	sub_dist = int(raw_input('Is it a sub distributor? : '))
	
	if sub_dist:
		parent_id = int(raw_input('Enter Parent ID : '))
	else:
		parent_id = -1
	co_list_i = []
	ci_list_i = []
	pr_list_i = []
	co_list_e = []
	ci_list_e = []
	pr_list_e = []

	n_cities,n_provinces,n_countries = map(int, raw_input('Enter number of cities, provinces and countries you want to include : ').split(','))
	for i in xrange(n_cities):
		ci_list_i.append(search(raw_input(),1))
	for i in xrange(n_provinces):
		pr_list_i.append(search(raw_input(),2))
	for i in xrange(n_countries):
		co_list_i.append(search(raw_input(),3))

	n_cities,n_provinces,n_countries = map(int, raw_input('Enter number of cities, provinces and countries you want to exclude : ').split(','))
	for i in xrange(n_cities):
		ci_list_e.append(search(raw_input(),1))
	for i in xrange(n_provinces):
		pr_list_e.append(search(raw_input(),2))
	for i in xrange(n_countries):
		co_list_e.append(search(raw_input(),3))

	distributor_list.append(distributor(co_list,ci_list,pr_list,co_list_e,ci_list_e,pr_list_e))

def show_distributor():
	for i in distributor_list:
		print i.i_cities,i.distributor_id

def read_file():
	with open('cities.csv', 'rb') as csvfile:
		return list(csv.reader(csvfile))[1:]

def main():
	cities_list = read_file()

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
	
	while 1:
		option = int(raw_input())
		if option == 0:
			break
		elif option == 1:
			add_distributor()
		elif option == 2:
			show_distributor()
			
if __name__ == '__main__':
	main()