import csv

distributor_list = []
location_list = []
file = open("distributor_list.txt", 'a')

def print_help():
	print "\t\t***Real Image Challenge 2016***"
	print " Features : "
	print " 1. Add a distributor and required permissions"
	print " 2. Show distributor permissions"
	print " 3. Check distributor permission for a location"
	print " SYNTAX"
	print " ADD DISTRIBUTOR DISTRIUBTOR_NAME"

def show_distributor_details(distributor):
	print distributor['NAME']
	print 'INCLUDE : '
	print distributor['INCLUDE']
	print 'EXCLUDE : '
	print distributor['EXCLUDE']

def read_file():
	with open('cities.csv', 'rb') as csvfile:
		list_val = list(csv.reader(csvfile))[1:]
	count=0
	for item in list_val:
		each_item = [count, item[0], item[1], item[2]]
		location_list.append(each_item)
		count+=1

def get_code(location):
	location_split = location.split('-')
	code_list=[]
	if len(location_split)==3:
		for place in location_list:
			if place[1] == location_split[0] and place[2] == location_split[1] and place[3] == location_split[2]:
				code_list.append(place[0])

	elif len(location_split)==2:
		for place in location_list:
			if place[2] == location_split[0] and place[3] == location_split[1]:
				code_list.append(place[0])

	elif len(location_split)==1:
		for place in location_list:
			if place[3] == location_split[0]:
				code_list.append(place[0])
	return code_list

def add_distributor(name, subdist=False, sublist=[], excludelist=[]):
	distributor = {}
	distributor['NAME'] = name
	distributor['EXCLUDE'] = []
	distributor['INCLUDE'] = []
	distributor['SUBDISTRIBUTOR'] = False
	distributor['SUBLIST'] = []
	while True:
		input_string2 = raw_input()
		if input_string2 == '':
			distributor_list.append(distributor)
			break
		else:
			command_variables = input_string2.split(' ')

			if command_variables[0] == 'INCLUDE':

				val = get_code(command_variables[1])
				if subdist:
					if set(val).issubset(set(sublist)) and not set(val).issubset(set(excludelist)):
						print "Allowed!"
						for num in val:
							distributor['INCLUDE'].append(num)
					else:
						print "Not Allowed!"
				else:
					for num in val:
						distributor["INCLUDE"].append(num)
			elif command_variables[0] == 'EXCLUDE':
				val = get_code(command_variables[1])
				for num in val:
					distributor['EXCLUDE'].append(num)
				for item in distributor['EXCLUDE']:
					if item in distributor['INCLUDE']:
						distributor['INCLUDE'].remove(item)

def add_subdistributor(command):
	if len(command)<3:
		print "Syntax Error"
		return
	child = command[1]
	parent = command[2]

	for distributor in distributor_list:
		if distributor['NAME'] == parent:

			distributor_exists=True
			add_distributor(child,True, distributor['INCLUDE'], distributor['EXCLUDE'])
	if not distributor_exists:
		print "No Distributor Found!"
		return
	
def check(distributor, location):
	location_code = set(get_code(location))
	included_locations = set(distributor['INCLUDE'])
	if location_code.issubset(included_locations):
			print "Yes, It is included!"
			return True
	print "No, It is not included!"
	return False

def check_rights(command):
	location_to_check=command[2]
	distributor_name = command[1]
	for distributor in distributor_list:
		if distributor['NAME'] == distributor_name:
			return check(distributor, location_to_check)

def main():
	read_file()
	while True:
		input_string = raw_input("\nEnter Command : ")
		command = input_string.split(' ')
		if command[0] == 'ADD':
			if len(command) < 3:
				print "Syntax Error"
			else:
				add_distributor(command[2])
		elif command[0] == 'EXIT':
			for distributor in distributor_list:
				file.write(str(distributor))
				file.write("\n")
			exit()
		elif command[0] == 'SHOW':
			if len(command)>1:
				for distrib in distributor_list:
					if command[1] == distrib['NAME']:
						show_distributor_details(distrib)
			else:
				print distributor_list
		elif command[0] == 'CHECK':
			check_rights(command)
		elif command[0] == 'HELP':
			print_help()
		elif command[0] == 'SUBDISTRIBUTE':
			add_subdistributor(command)


if __name__ == '__main__':
	main()