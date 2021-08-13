class Employee:
    name: str
    emp_id: int
    age: int
    city: str

    def __init__(self, name, emp_id, age, city) -> None:
        self.name = name
        self.emp_id = emp_id
        self.age = age
        self.city = city

    def __repr__(self) -> str:
        return (f"Employee (name={self.name})")

    def __eq__(self, check) -> bool:
        return ((self.name, self.age, self.emp_id, self.city) ==
                (check.name, check.age, check.emp_id, check.city))


e1 = Employee('Abhijeet', 1, 33, "Pune")
e2 = Employee('Savitoj', 2, 34, "Punjab")
e3 = Employee('Aayush', 3, 8, "Mumbai")

print("Employee Details")
print(e1)
print(e2)
print(e3)

print(e1 == e2)
print(e1 == e1)
print(e3 == e2)