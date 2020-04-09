def import_text(inp_name):
    """
    This function reads the file with a given name
    :param inp_name: defines a name of source storing the text
    :type inp_name: str
    :return: text stored into given file
    :return: str
    """
    try:
        with open(inp_name, 'r') as file:
            text = file.read()
            
    except FileNotFoundError as error:
        print(error)
    except TypeError:
        print('only str is expected as an argument')
    
    return text


def export_text(output, filename):
    """
    This function writes its argument into file "result,txt"
    :param output: defines a name of source storing the text
    :param filename: name of resulting file
    :type output: str
    :type filename: str
    :return: file with output text inside
    :return: "result.txt"
    """
    try:

        with open(filename, 'a') as file:
            file.write(output)
            
    except TypeError:
        print('only str type can be used as an "export_text" arguments')
