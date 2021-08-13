from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    emp_id: int
    age: int
    city: str

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