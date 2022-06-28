import unittest
from import_this import Role, Employee, Manager, Supervisor, Post
import uuid

class MakingTest(unittest.TestCase):

    def test_employee_email(self):
        employee = Employee("Ron", "Weasley")
        found_employee = Employee.get_employee_by_email("ronw@codingtemple.com")
        self.assertEquals(found_employee.first_name, employee.first_name)

    def test_add_employee(self):
        manager = Manager("Lucas", "Lang")
        self.assertEquals(len(manager.employees), 0)
        employee = Employee("Meilani", "Nishimura")
        manager.add_employee(employee)
        self.assertEquals(len(manager.employees), 1)
        
    def test_remove_employee(self):
        manager1 = Manager("Lucky", "Lang")
        employee1 = Employee("Em", "Inem")
        manager1.add_employee(employee1)
        print(manager1.employees)
        print(len(manager1.employees))
        manager1.remove_employee(employee1)
        self.assertEquals(len(manager1.employees), 0)

        print(len(manager1.employees))

    def test_make_post(self):
        p = Post("Hello world", "samples@codingtemple.com")
        self.assertIn(p, p.all_)


unittest.main(MakingTest())

        



