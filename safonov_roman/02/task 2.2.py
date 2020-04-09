user_input = input ('enter string which you want to reverse: ')
reversed_list = []

#v.1

print ('\n', end='')

for i in range (1, len (user_input)+1):
    reversed_list.append (user_input[-i])

for element in reversed_list:
    print (element, end='')


#v.2

print ('\n')

reversed_list = [user_input[-i] for i in range (1,len(user_input)+1)]

for element in reversed_list:
    print (element, end='')
       
