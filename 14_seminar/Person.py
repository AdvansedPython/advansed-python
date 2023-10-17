class Person:

    def __init__(self, first_name, second_name, theard_name, age):

        self.first_name = first_name
        self.second_name = second_name
        self.theard_name = theard_name
        self.age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age
        

class Employee(Person):

    def __init__(self, first_name, second_name, theard_name, age, id):

        if not (100_000 < id <  999_999):
            raise InvalidIdError(f'Invalid id: {id}. Id should be a 6-digit positive integer between 100000 and 999999.')

        super().__init__(first_name, second_name, theard_name, age)
        self.id = id

    def get_level(self):
        
        return sum([int(x) for x in str(self.id)]) % 7
    




class InvalidNameError(Exception):
    
    def __init__(self, msg):
        self.msg = msg
        
    def __str__(self):
        return self.msg
    

class InvalidAgeError(Exception):
    
    def __init__(self, msg):
        self.msg = msg
        
    def __str__(self):
        return self.msg


class InvalidIdError(Exception):
    
    def __init__(self, msg):
        self.msg = msg
        
    def __str__(self):
        return self.msg