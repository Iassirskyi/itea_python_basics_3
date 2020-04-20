try:
    File = open ('sample_text.txt', 'r')
    Text = File.readline()

    def convert(string):
        
        low = string.lower()
        transformed_list = list(low.split(" "))
        return transformed_list


    def punctuation(PunctMarks):
     
        punctuation_marks = ['.',',',':',';','!','?','(',')'] 

        List_without_punctuation = []
        for word in PunctMarks:
            if word[-1] in punctuation_marks:
                List_without_punctuation.append(word[:-1])
            elif word[0] in punctuation_marks:
                List_without_punctuation.append(word[1:])
            else:
                List_without_punctuation.append(word)

        return List_without_punctuation

    def spec_words(stopList):

        spec_words_list = ['a', 'an', 'to', 'is', 'are', 'was', 'were', 'will', 'would', 'could', 'and', 'or', 'if', 'he', 'she', 'it', 'this', 'my', 'etc']
        for word in list(stopList):
            if word in spec_words_list:
                stopList.remove(word)
         
        SpecList= stopList
        
        return SpecList

    def frequency(wordList):
      
        wordfreq = []
        
        for i in wordList:
            wordfreq.append(wordList.count(i) / len(wordList) * 100)

        return wordfreq

    list_of_words = convert (Text)
    no_punctuation = punctuation(list_of_words)
    no_spec_words = spec_words(no_punctuation)

    print('Words quantity: ', len(no_spec_words))
    print('Text dictionary: ', ', '.join(list(dict.fromkeys(no_spec_words))))

    note_word = {i:no_spec_words.count(i) for i in no_spec_words}

    print('Keywords:', end = ' ') 
    j = 0
    a = ',' #This was made for printing dot in the end of the keyword, cause I couldn`t find another way
    for key, value in sorted(note_word.items(), key=lambda item: item[1], reverse = True):
        print("%s - %s" % (key, value), end = f'{a} ')
        j += 1
        if j == 2:
            a = '.'
        if j >= 3:
            break
        
    print('\nFrequency:', end = ' ')
    freq = frequency(no_spec_words)
    for i in range(len(no_spec_words)):
        A = print(f'{no_spec_words[i]} - {freq[i]}%', end = ', ')
        
    File.closed
    
    
    with open('results.txt', 'w') as Finish :
        
        print(Finish.write(str(A)))
        
    
    
except ValueError as error:
    print (error)
