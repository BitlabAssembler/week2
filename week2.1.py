lst = [1, 2, 3, 4, 5, 6, 7]




def length(lst):
    counter = 0
    print('here')
    while True:
        try:
            lst[counter]
            counter += 1
        except IndexError:
            break    
    print(counter)
    return counter


def reverse(lst):
    ln = length(lst)
    result = [0] * ln
    for i in range(ln):
        result[i]= lst[ln - 1 - i]

    print(lst)
    print(result)


def append(extra_item):
    ln = length(lst)
    result = [0] * (ln + 1)
    for i in range(ln):
        print(i)
        result[i] = lst[i]
    
    result[ln] = extra_item
            
    print(lst)
    print(result)


reverse(lst)
getal = 8
append(getal)
