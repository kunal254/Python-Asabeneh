import re

def is_valid_variable(var):
    reg = r'(^\d|[^A-Za-z0-9_])'
    print(not bool(re.search(reg, var)))

is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True

is_valid_variable('34firstname') # False
is_valid_variable('firstname34_3') # True
