from dataclasses import dataclass, field

def default_age():
    return 33

def default_hobbies():
    return ['Chess']

@dataclass
class Employee:
    name: str = field(compare=False)
    emp_id: int = field(compare=False)
    age: int = field(default_factory=default_age, compare=True)
    city: str = field(default='Pune', compare=False)
    hobbies: list[str] = field(default_factory=default_hobbies, repr=False, compare=False)
    
e1 = Employee('Abhijeet', 1)
e2 = Employee('Abhijeet1', 2)

print("Employee Details")
print(e1)
print(e2)
print(e1 == e2)
