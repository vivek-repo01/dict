# Initialize dictionary with default values

#In Python, we can initialize the keys with the same values.

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

res = dict.fromkeys(employees, defaults)
print(res)

#The dict.fromkeys() method in Python is used to create a new dictionary with keys from an iterable (in this case, employees) and all values set to a specified default value (defaults). Here's how it works:

#employees is a list containing the keys for the new dictionary.
#defaults is the default value that will be assigned to all keys in the new dictionary.

#The dict.fromkeys(employees, defaults) call creates a new dictionary where each key is taken from the employees list, and all corresponding values are set to the specified defaults value. In this case, the resulting dictionary res has keys 'John', 'Jane', and 'Bob', each associated with the default value of 0.

#This method is useful when you want to initialize a dictionary with a default value for all keys, especially when you want all keys to share the same initial value.