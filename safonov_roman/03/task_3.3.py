
              
def filter_cust (func, sequence):
    """
    This function is analog of build in "filter" function.
    :param func: is a function which verify each element of sequence
        on specified condition
    :param sequence: is a list of iterable elements which are passed
        as an argument to "func" one by one
    :type func: def
    :type sequence: int/str/bool/list/tuple
    :return: filter_cust returns list of sequence elements
        which meets condition described into func
    :return: list
    """
    output_list = []
    
    for i in range (len(sequence)):
        if func(sequence[i]):
            output_list.append (sequence[i])

    return output_list


def odd_check (a):
    answer = a % 2

    return answer


def upper_chk (a):
    if a == a.upper():
        answer = 1
    else:
        answer = 0

    return answer


print (filter_cust (odd_check, [1, 2, 3, 4, 5]))
print (filter_cust (upper_chk, ['A', 'B', 'C', 'd', 'E']))
print (filter_cust (lambda x: x % 2, [1, 2, 3, 4, 5]))

