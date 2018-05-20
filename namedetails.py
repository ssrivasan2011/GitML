import logging
logging.basicConfig(format='%(asctime)s %(name)s %(message)s',level=logging.INFO)
logger=logging.getLogger('Details')
 
class abc(object):
    def __init__(self,name):
        self.name=name
    def fnc(self,surname):
        nameList=[]
        logger.info('name of the person {}'.format(self.name+surname))
        nameList.append(self.name+surname)
        logger.info('The value of list is delared {}'.format(nameList))

object=abc('Aashrith')
object.fnc('kesh')
object1=abc('Sampada')
object1.fnc('g')
        
        