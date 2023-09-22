def remove_every_other(my_list):
    new_list = []
    for i in my_list[::2]:
        new_list.append(i)
    return new_list