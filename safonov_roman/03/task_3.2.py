
              
def map_cust (func, *args):
    """
    This function is a try to do something alike to built in "map" function
    :param func: is a function which is performed by map_cust and uses "*args" as it's arguments
    :param args: is a list of arguments with the same length
    :type func: function
    :type args: list/tuple
    :return: return the list of values which returns "func" with each value from "*args" as an agrument
    :return: list
    """

    squence = []
    output_list = []
    
    if len(args) == 1:
        sequence = args[0]
    
        for i in range (len(sequence)):
            iteration = func(sequence[i])
            output_list.append (iteration)

    elif len(args) > 1:
        sequence_1 = args[0]
        sequence_2 = args[1]
        
        
        def input_generator (i):

            input_list = []
            
            for j in range (len(args)):
                input_list.append (list(args[j])[i])
                
            return input_list

        
        for i in range (len(args[0])):
            
            iteration = func(*input_generator(i))
            output_list.append (iteration)

    return output_list    


def function_1 (a):
    a = int (a) ** 2
    return a

def function_2 (a):
    a = str(a).upper()
    return a

print (map_cust(function_1, [1, 2, 3, 4, 5]))
print (map_cust(function_2, 'abcd'))
print (map_cust(lambda x: x**2, (1, 2, 3, 4, 5)))
print (map_cust(lambda x,y,z: x * y + z, [1, 2, 3, 4, 5], [2, 2, 2, 2, 2],[1, 1, 1, 1, 1]))

