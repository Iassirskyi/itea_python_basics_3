list = [1, 2, 3, 1, 3, 2, 1]
counter = 0
entries_count = []


#v.1

for number in list:

    for i in range (len(list)):
        if number == list[i]:
            counter += 1

    entries_count.append (counter)
    counter = 0

for i in range(len(entries_count)):
    if entries_count[i] % 2:
        print (f'{list[i]}')
        break

#v.2

for number in list:
    
    for i in range(len(list)):
        if number == list[i]:
            counter += 1
                        
    if counter % 2:
        print (f'{number}')
        break

