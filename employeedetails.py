# Lets create a class to get the details of employee from organisation

class Employee(object):
	def __init__(self,employeeName,ID,salary,designation):
		self.employeeName = employeeName
		self.ID= ID
		self.salary=salary
		self.designation=designation
		## Add other basic details of employee
		
	
	def department(self):
		employeeDepartment = list()
		list=['HR','Coding','Testing']
		print list
		print list[0]
		print list[1]
		print list[2]
		## create the departments the employee worked with the organisation,
		## EX: create 3 departments: HR, TESTING AND CODING.
		## It should PRINT that list.

	def personalDetails(self):
		dict= {}
		cdict= {'age' : 29,'name' : abcd, 'city' : Bangalore}
		print cdict
		print cdict.keys()
		print cdict.values()
                ## Create a key value pair of personal details.
                ## ex:{'age':32}
                ## It should PRINT that dictionary of all the personal details.

