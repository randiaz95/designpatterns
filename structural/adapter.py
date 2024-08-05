# TODO WRAP THIS UP INTO A CORRECT PATTERN. THIS IS JUST A SIMPLE EXAMPLE

# Target interface
class Target:
    def request(self):
        pass

# Adaptee class
class Adaptee:
    def __init__(self):
        self.data = "1"

# Adapter class
class Adapter(Target):
    def __init__(self, adaptee):
        # Modify adaptee someway to fit the target interface
        self.output = self.transform(adaptee)

    def transform(self, adaptee):
        return int(adaptee.data)

    def request(self):
        print(f"Do something with data: {self.output}")

if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    adapter.request()