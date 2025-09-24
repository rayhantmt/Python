bird=["Parrot","John","lea"]
bird.extend(["Crow","cow","hipopotemas","a"])
print(bird)
print('The extend function adds another list with the list')
bird.insert(3,"a")
print('The insert function adds an element at a specific position of the list')
print(bird)
x=bird.pop()
print('The pop function returns the last element and removes it from the list')
print(x)

print(bird)
bird.sort(key=str.upper())
print(bird)