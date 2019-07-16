

class Employee:
    """
    Employee class
    """
    employee_count = 0

    def __init__(self, first_name=None, last_name=None, pay=1000., rank=0):
        self.firstName = first_name
        self.lastName = last_name
        self.rank = rank
        self.salary = pay
        self.email = None
        if(self.firstName is not None and self.lastName is not None):
            self.email = f"{self.firstName}.{self.lastName}@something.com"
            
        Employee.employee_count += 1

    @classmethod
    def __init_cls__(cls, employee_count):
        emp = cls(None, None, 0, 0)
        cls.employee_count = employee_count
        return emp

    @staticmethod
    def is_even_or_odd(day):
        if day < 0 or day > 6:
            raise ValueError("Input out of bounds. Expecting a number between 0 and 6")
        if day % 2 == 0:
            print("True")
            return True
        return False

    def promote(self):
        self.rank += 1

    def raise_salary(self, value):
        self.salary += value

    @property
    def first_name(self):
        return self.firstName

    @first_name.setter
    def first_name(self, value):
        self.firstName = value

    def __repr__(self):
        email = ""
        if self.email is None:
            email = ""
        return(f""" Employee
            firstName: {str(self.firstName)}
            lastName: {str(self.lastName)}
            rank: {str(self.rank)}
            salary: {str(self.salary)}
            email: {str(email)}
            number of employees: {Employee.employee_count}
        """)

    @classmethod
    def increment_count(cls):
        cls.employee_count += 1


class Ballerina(Employee):
    """
    Ballerina class
    """
    employee_count = 0

    def __init__(self, first_name=None, last_name=None, pay=1000., rank=0, dances=[]):
        super().__init__(first_name, last_name, pay, rank)
        self.dances = dances
        Ballerina.employee_count = 5
        
    def __repr__(self):
        s = super().__repr__()
        s = f"{s} dances {self.dances}"
        return s

    @classmethod
    def increment_count(cls):
        cls.employee_count += 2
