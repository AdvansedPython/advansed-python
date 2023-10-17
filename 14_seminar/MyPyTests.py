import pytest
from Person import Person
from Person import Employee


@pytest.fixture
def set_human():   
    return Person("Jack", "Lee", "Olegovich", 30)

@pytest.fixture
def set_employee():
    return Employee("Jack", "Lee", "Olegovich", 30, 100_001)


        
def test_create_person(set_human):
    assert isinstance(set_human, Person)


def test_birthday(set_human):
    human = set_human
    human.birthday()
    assert human.age == 31


def test_create_employee(set_employee):
    assert isinstance(set_employee, Employee)


def test_get_level(set_employee):
    employee = set_employee
    assert set_employee.get_level() == 2



if __name__ == '__main__':
    pytest.main(['-v'])