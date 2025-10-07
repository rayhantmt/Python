def cunter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment
increment=cunter()
print(increment())
print(increment())
print(increment())
print(increment())
