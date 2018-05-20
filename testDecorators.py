import logging
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.ERROR)
logger=logging.getLogger('decorator')



def secondclass(testfunct):
    def wrapper(abc):
        a=testfunct(abc)
        logger.error(a+ 'thrdclass')
    return wrapper

@secondclass
def thrdclass(abc):
    return('decorator log')
     

thrdclass('abc')
