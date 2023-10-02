class Fabrica:
    
    
    def animal_class(type: str, name: str, age: int, spec: str):
        match type.lower():

            case "cat":
                return Cat(name, age, spec)
            case "dog":
                return Dog(name, age, spec)
            case "fish":
                return Fish(name, age, spec)
            case _:
                return Animal(name, age)




class Animal:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.type = "unknown"
        self.spec = None


    def get_info(self):
        return f"Тип - {self.type}, Имя - {self.name}"


class Cat(Animal):

    def __init__(self, name: str, age: int, spec: str):
        super().__init__(name, age)
        self.type = "cat"
        self.spec = spec


class Dog(Animal):


    def __init__(self, name: str, age: int, spec: str):
        super().__init__(name, age)
        self.type = "dog"
        self.spec = spec


class Fish(Animal):


    def __init__(self, name: str, age: int, spec: str):
        super().__init__(name, age)
        self.type = "fish"
        self.spec = spec