def cunter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment
increment1=cunter()
increment2=cunter()
print(increment1())
print(increment1())
print(increment1())
print(increment2())
