import threading
import re
import os
import string

# character sets allowed in the string
chars = string.ascii_letters + string.digits + string.whitespace + string.punctuation


# Function to strip all but ascii letters, digits, and whitespace
def clean(inString, allowed_list=chars):
    '''
        Cleans string passed in as a parameter from non-ascii characters,
        punctuation, blank lines, nultiple spaces, and converts all the
        words in the string to lower case. Returns a dictionary of 
        word counts in the string.
    '''
    # Isolate ascii chars only
    temp = ''.join([i if ord(i) < 128 else ' ' for i in inString])
    
    # Remove punctuation. # make sure to use str() to get rid of unicode
    replace_punctuation = string.maketrans(string.punctuation, ' ' * len(string.punctuation))
    temp = str(temp).translate(replace_punctuation)

    # Remove blank lines
    temp = os.linesep.join([s for s in temp.splitlines() if s])

    # Remove extra spaces
    temp = re.sub(' +',' ', temp)

    # Convert temp to lower case
    temp = temp.lower()

    # Create a dictionary to return
    to_return = {}
    
    # Split string
    tmp_list = temp.split()
 
    # Populate the dictionary to return
    for word in tmp_list:
        word = word.strip()
        if word in to_return:
            value = to_return[word]
            to_return[word] = (value + 1)
        else:
            to_return[word] = 1
 
    # Return dictionary
    return to_return


# merging list of dictionaries
def mergedicts(lst):
    '''
        Merges a list of dictionaries into a single dictionary and
        returns newly constructed dictionary.
    '''
    my_dict = {}

    for dict_in_list in lst:
        for i in dict_in_list:
            if i in my_dict:
                value = my_dict[i]
                my_dict[i] = (value + dict_in_list[i])
            else:
                my_dict[i] = dict_in_list[i]
    return my_dict

