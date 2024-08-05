# Singleton pattern 
# - is used when you want to eliminate 
# the option of instantiating more than one object.
# - Return existing global instance or create a new one.
class Singleton:
    _instance = None

    # PUBLIC STATIC VOID INITIALIZER
    # DUNDER METHOD
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    # __init__ is called after __new__ if __new__ returns an instance of cls
    # __init__ is the constructor
    # __new__ is the initializer
    # __new__ is the first step of instance creation

if __name__ == "__main__":
    singleton1 = Singleton()
    singleton2 = Singleton()

    # SomeClass.staticMethod()
    # someInstance = SomeClass()
    # someInstance.instanceMethod()

    print(singleton1 is singleton2)