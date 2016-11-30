class Singelton(type):
    _instances = {}
    def __call__ (cls,*args,**kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singelton, cls).__call__(*args, **kwargs)
            cls.x=5
        return cls._instances[cls]

class MyClass(object):
    __metaclass__ = Singelton


m = MyClass()
v = MyClass()

print m.x
m.x = 9
print v.x