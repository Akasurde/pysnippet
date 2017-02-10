import string

value = {'var': 'abhijeet'}

t = string.Template("""
Variable : $var
Escape   : $$
Variable in text : ${var}iable
""")

print("TEMPLATE :" , t.substitute(value))
