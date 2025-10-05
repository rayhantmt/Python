Boidata={'name':'Rayhan','age':23,'gender':'male'}
print(Boidata)
print(Boidata.keys())
print(Boidata.values())
print(Boidata['age'])
Boidata['age']=2
print(Boidata)
print(Boidata.get('color','Blue'))
Boidata.pop('age')
#pop will return and delete the item form the dict

print(Boidata)
Boidata['sex']='straight'#method to add a new item in the dict
del Boidata['name']#method to delete an element form the dict

print(Boidata)
#using the list method helps to get the keys as a list
print(list(Boidata.keys()))
