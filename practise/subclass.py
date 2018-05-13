from classexamples import first

class second(first):
    def __init__(self,name,age,adress,employement):
        super().__init__(name=name,age=age,adress=adress)
        self.employement = employement
        
    def employementDetails(self):
        self.personalDetails()
        print('The employement status of the preson is %s' %(self.employement))
        
        
obj = second('ajay',30,'Bangalore','jobless')
obj.employementDetails()