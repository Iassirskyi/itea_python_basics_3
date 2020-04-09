from imp_exp import import_text, export_text


EXCEPTIONS = ('of', 'for', 'the', 'a', 'as', 'an', 'at', 'the', 'in', 'to', 'is', 'are', 'was', 'were', 'will', 'would', 'could', 'and', 'or', 'if', 'he', 'she', 'it', 'this', 'my')
PUNCTUATIONS = ('+', '-', '&', '.', '!', '?', ',', ':', '—', '–', '“', '”', '"', '(', ')', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '$')


def prettify_text(text):
    """
    This function removes from text specified exceptions and converts it into list
    :param text: unformated initial text
    :type text: str
    :return: cleaned elements of text
    :return: list
    """
    try:
        for element in PUNCTUATIONS:
            text = text.replace(element, '')

        text = text.lower().split()
        clean_text = text.copy()

        for element in text:
            if element in list(EXCEPTIONS):
                clean_text.remove(element)
           
        return clean_text
    except NameError:
        print('to use this function you needs the following constants: "EXCEPTIONS" and "PUNCTUATIONS".')

def words_count (text):
    try:
        if type(text) is not list:
            raise TypeError

        return len (text)
    except TypeError:
        print('only text formated as a list can be used as an argument')
    
    

def unique_words (text):
    """
    This function generate a list of unique elements of text in alphabetical order
    :param text: is a text formated as a list of elements 
    :type text: list
    :return: set of unique elements
    :return: set
    """
    text_dict = set(text)
    text_dict = sorted(text_dict)
    return text_dict

    
def f_words (text):
    """
    This function returns the most frequent elements of the text and quantity of it's occurance
    :param text: list of text elements 
    :type text: list
    :return: top 3 most frequent elements of the text and quantity of it's occurance
    :return: tuple
    """
    def counter (element):
        return text.count(element)
           
    frequency_list = sorted(unique_words(text), key=counter, reverse=True)
    
    top_1 = frequency_list[0], counter(frequency_list[0])
    top_2 = frequency_list[1], counter(frequency_list[1])
    top_3 = frequency_list[2], counter(frequency_list[2])
    
    return top_1, top_2, top_3


def frequency_calculation (element, text):
    """
    This function calculates percentage of element's occurance into text
    :param element: some element of the text
    :param text: list of text elements
    :type element: str
    :type text: list
    :return: percentage of element's occurance into text
    :return: float
    """
    basic_len = len(text)
    unique_list = unique_words(text)
    percentage = (text.count(element) / basic_len)

    return percentage

if __name__ == '__main__':

    initial_text = import_text('text.txt')
    normalized_text = (prettify_text(initial_text))
    result = []

    result = (f'This text consists of {words_count(normalized_text)} words.')
    result += '\n\nHere are those words: '
    
    for element in unique_words(normalized_text):
        result += element.capitalize()
        result += ', '
                
    result += '\n\nThree most frequent words in this text are: '
    for i in range (3):
        if f_words(normalized_text)[i][1] == 1:
            result += f'\n{i+1}) Word "{(f_words(normalized_text)[i][0]).capitalize()}" meets {f_words(normalized_text)[i][1]} time;'
        else:
            result += f'\n{i+1}) Word "{(f_words(normalized_text)[i][0]).capitalize()}" meets {f_words(normalized_text)[i][1]} times;'

    result += '\n\nHere is the frequency of each unique word in this text:'
    for element in unique_words(normalized_text):
        percentage = frequency_calculation(element, normalized_text)
        result += f'{element} - {percentage:.2%}'
        result += ', '

    export_text (result, 'result.txt')
    print ('all done')
