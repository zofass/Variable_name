import string
import keyword
action = input("Please enter the variable name: ")
def is_valid_variable_name(variable_name):
    if variable_name and variable_name[0].isdigit():
        return False

    if variable_name.isdigit():
        return False

    if not all(char.islower() or char.isdigit() or char == "_" for char in variable_name):
        return False

    if variable_name.count("_") == 1 and len(variable_name) > 1 and variable_name[0] != "_":
        return True

    if variable_name in keyword.kwlist:
        return False

    return True

print(is_valid_variable_name(action))
