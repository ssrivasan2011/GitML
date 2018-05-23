from classexamples import first
from familydetails import family


class second(first,family):
    def __init__(self,name,age,adress,employement,status):
        super().__init__(name=name,age=age,adress=adress)
        self.employement = employement
        self.status=status
        
    def employementDetails(self):
        self.personalDetails()
        self.hasChild()
        print('The employement status of the preson is %s' %(self.employement))
        
        
obj = second('ajay',30,'Bangalore','jobless','married')
obj.employementDetails()