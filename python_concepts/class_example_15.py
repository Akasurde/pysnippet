from dataclasses import dataclass, field

def default_age():
    return 33

@dataclass
class Employee:
    name: str
    emp_id: int
    age: int = field(default_factory=default_age)
    city: str = field(default='Pune')

e1 = Employee('Abhijeet', 1)

print("Employee Details")
print(e1)