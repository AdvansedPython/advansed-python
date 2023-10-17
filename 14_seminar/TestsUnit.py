import unittest
from Person import Person
from Person import Employee

class TestUnitMyPerson(unittest.TestCase):

    def setUp(self):
        self.human = Person("Jack", "Lee", "Olegovich", 30)
        self.employee = Employee("Jack", "Lee", "Olegovich", 30, 100_001)

        
    def test_create_person(self):
        self.assertIsInstance(self.human, Person)

    def test_birthday(self):
        self.human.birthday()
        self.assertEquals(self.human.age, 31)


    def test_create_employee(self):
        self.assertIsInstance(self.employee, Employee)

    def test_get_level(self):
        self.assertTrue(self.employee.get_level() == 2)



if __name__ == '__main__':
    unittest.main(verbosity=2)