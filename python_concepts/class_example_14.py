from dataclasses import dataclass, field

@dataclass
class Employee:
    name: str
    emp_id: int
    age: int
    city: str = field(default='Pune')

e1 = Employee('Abhijeet', 1, 33)

print("Employee Details")
print(e1)