class List:
    def remove_(self, integer_list, values_list):
        lst = []
        for i in integer_list:
            lst.append(i)
        for j in lst:
            if j in values_list:
                lst.remove(j)
        return lst