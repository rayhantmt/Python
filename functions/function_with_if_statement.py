def chose(computer,human):
    print(f'computer is {computer} and human is {human}')
    if computer != human:
        print('computer and human are equal')
    return computer+human
chose('electricity','pizza')
def chose(computer,human):
    if computer != human:
        print('computer and human are equal')
        return computer+human
    return computer
chose('electricity','pizza')
def chose(computer,human):
    if computer == human:
        print('computer and human are not equal')
