from dataclasses import dataclass, field

def default_age():
    return 33

def default_hobbies():
    return ['Chess']

@dataclass
class Employee:
    name: str
    emp_id: int
    age: int = field(default_factory=default_age)
    city: str = field(default='Pune')
    # hobbies: list[str] = field(default=['Chess'])  # Raises ValueError: mutable default <class 'list'> for field hobbies is not allowed: use default_factory
    hobbies: list[str] = field(default_factory=default_hobbies)
    
e1 = Employee('Abhijeet', 1)

print("Employee Details")
print(e1)