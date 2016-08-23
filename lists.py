lst = ['a', 'b', 'd', 'c']
def delete_element(element):
    lst.remove(element)
    return lst
print delete_element('c')

def lenght_of_list():
    return len(lst)
print lenght_of_list()

def find_element_of_list(element):
    return (element in lst)

def find_element_of_list_v2(param_element):
    is_found = False
    for element in lst:
        if element == param_element:
            is_found = True
    return is_found

print find_element_of_list('a')
print find_element_of_list('b')
print find_element_of_list('c')
print find_element_of_list('d')
print find_element_of_list('f')

def append_element(element):
    lst.append(element)
    return lst
print append_element('f')

def sorted_list():
    lst.sort()
    return lst
    # return lst.sort()
print sorted_list()
