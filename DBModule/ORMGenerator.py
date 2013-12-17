import importlib

class ORMGenerator:
    def __init__(self, module):
        self.__module = module
        

    def class_for_name(self, class_name):
        # load the module, will raise ImportError if module cannot be loaded
        m = importlib.import_module(self.__module)
        # get the class, will raise AttributeError if class cannot be found
        try:
            c = getattr(m, class_name)
        except AttributeError, e:
            print e
        else:
            return c
    
    
    