from dataclasses import dataclass, field

def default_age():
    return 33

@dataclass
class Employee:
    name: str
    emp_id: int
    age: int = field(default_factory=default_age)
    city: str = field(default='Pune')
    hobbies: str = field(init=False)

    def __post_init__(self):
        print("I am called - post_init")
        self.hobbies = 'Chess'

e1 = Employee('Abhijeet', 1)

print("Employee Details")
print(e1)