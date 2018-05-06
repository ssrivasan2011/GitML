# Lets create a class to get the details of employee from organisation

class Employee(object):
	def __init__(self,employeeName):
		self.employeeName = employeeName
		## Add other basic details of employee
		
	
	def department(self):
		employeeDepartment = dict()
		## create the departments the employee worked with the organisation,
		## EX: create 3 departments: HR, TESTING AND CODING.

