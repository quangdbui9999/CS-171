
def block(names, blocked):
    new_list = []
    set_names = set(names)
    set_blocked = set(blocked)
    new_set = set_names.difference(set_blocked)
    new_list = list(new_set)
    new_list = sorted(new_list, reverse = False)
    return new_list

list_names = ['HTML', 'CSS', 'Javascript','Mysql', 'SQl-Server', 'PHP', 'Python', 'C', 'C++', 'HTML5', 'CSS3']
block_name = ['Javascript', 'Mysql', 'CSS', 'C']
print(block(list_names, block_name))



