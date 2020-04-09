user_input = input ('enter string to check: ')
char_count = len (user_input)


#v.1

o_count = 0
x_count = 0


for i in range(char_count):
    if user_input [i] == 'o' or user_input [i] == 'O':
        o_count += 1
    elif user_input [i] == 'x' or user_input [i] == 'X':
        x_count += 1
    
print (f'v.1 says {o_count == x_count}')


#v.2

o_count = 0
x_count = 0


for i in range(char_count):
    if 'o' in user_input [i] or 'O' in user_input [i]:
        o_count += 1
    elif 'x' in user_input [i] or 'X' in user_input [i]:
        x_count += 1
           
print (f'v.2 says {o_count == x_count}') 


#v.3

o_count = 0
x_count = 0


for letter in user_input:
    if letter == 'o' or letter == 'O':
        o_count += 1
    elif letter == 'x' or letter == 'X':
        x_count += 1
      
print (f'v.3 says {o_count == x_count}')
