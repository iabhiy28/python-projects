#deleting elements of the dictionary
# Creating a Dictionary 
Dict = {'Dict1': {1: 'Geeks'}, 
        'Dict2': {'Name': 'For'}} 
del(Dict['Dict2'])
print(Dict)
# Accessing element using key 
print(Dict['Dict1']) 
print(Dict['Dict1'][1]) 
# print(Dict['Dict2']['Name']) 