

def array_diff (f_list,s_list):
    """
    This function returns list of elements from f_list which are not met into s_list
    :param f_list: is a list of values which needs to be verified
    :param s_list: is a list of values which will be substracted from the f_list
    :type f_list: list/tuple/str
    :type s_list: list/tuple/str
    :return: list of values from f_list, which are not present in s_list
    :return: list
    """

    output_list = []
    
    for i in range (len(f_list)):
        remove = 0
        
        for j in range (len(s_list)):
            if f_list[i] == s_list[j]:
                remove = 1

        if not remove:
            output_list.append (f_list[i])

    return output_list    


print (array_diff ([1, 2], [1]))
print (array_diff ([1, 2, 2, 2, 3], [2]))
print (array_diff ((1, 2, 3),[2, 3]))
print (array_diff (['A', 'a', 'A', 'b', 'c'],['A']))
print (array_diff ('abc','a'))
print (array_diff (str(123),'2'))

