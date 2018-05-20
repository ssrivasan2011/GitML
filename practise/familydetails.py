class family(object):
    def __init__(self,status):
        self.status=status
    def  hasChild(self):
        if self.status=='married':
            print('Has Kids')
        elif self.status!='married':
            print('No Kids')
        else:
            print('No idea')


#object=family('not married')
#object.hasChild()

        