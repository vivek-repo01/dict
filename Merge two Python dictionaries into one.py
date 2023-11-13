#Merge two Python dictionaries into one

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = {**dict1, **dict2}
print(dict3)

#This line of code in Python is using the dictionary unpacking syntax (**)
#to merge the contents of two dictionaries (dict1 and dict2) into a new dictionary (dict3).
# Here's how it works:

#{**dict1, **dict2}: This syntax is used to unpack the key-value pairs from both dict1
#and dict2 and create a new dictionary (dict3) that includes all the key-value pairs from
# both dictionaries.
