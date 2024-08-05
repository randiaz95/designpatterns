# Prototype pattern 
# - is used when you want to create a new object.
# by copying an existing object.
# - Create a new object by copying an existing object.
class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **kwargs):
        obj = self._objects.get(name)
        if obj:
            # Create a clone
            cloned_obj = obj.clone()
            cloned_obj.__dict__.update(kwargs)
            return cloned_obj
        else:
            raise ValueError(f"Object with name '{name}' does not exist.")

    def get_objects(self):
        return self._objects


if __name__ == "__main__":
    class Object1:
        def __init__(self, a, b, c) -> None:
            a=a
            b=b
            c=c
    class Object2:
        def __init__(self, d, e, f) -> None:
            d=d
            e=e
            f=f

    prototype = Prototype()
    prototype.register_object('object1', Object1())
    prototype.register_object('object2', Object2())

    obj1 = prototype.clone('object1', a=1, b=2, c=3)
    obj2 = prototype.clone('object2', d=4, e=5, f=6)

    print(obj1)
    print(obj2)
