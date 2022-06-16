# this is single inheritance program
class person:
    def __init__(self, Name, Age, Address):
        self.Name = Name
        self.Age = Age
        self.Address = Address

    def display(self):
        print(f"Name: {self.Name}")
        print(f"Age:  {self.Age}")
        print(f"Address: {self.Address}")

class employee(person):
    def __init__(self, Name, Age, Address, eid, dept, salary):
        super().__init__(Name, Age, Address)
        self.eid = eid
        self.dept = dept
        self.salary = salary

    def display(self):
        super().display()
        print(f"Eid: {self.eid}")
        print(f"Dept: {self.dept}")
        print(f"Salary: {self.salary}")

e = employee("Swapnil", 30, "Ashta", 3003, "CSE", 40000)
e.display()
