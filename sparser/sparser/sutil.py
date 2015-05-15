import threading
import re
import os
import string

# character sets allowed in the string
chars = string.ascii_letters + string.digits + string.whitespace + string.punctuation

# Function to strip all but ascii letters, digits, and whitespace
def clean(inString, allowed_list=chars):
    # Isolate ascii chars only
    temp = "".join([ch for ch in inString if ch in allowed_list])
    
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


# Decorator called sycnronized that uses threading to synchroznise access
def synchronized(func):
    func.__lock__ = threading.Lock()
    def synced_func(*args, **kws):
        with func.__lock__:
            return func(*args, **kws)
    return synced_func

# merging list of dictionaries
def mergedicts(lst):
    my_dict = {}

    for dict_in_list in lst:
        for i in dict_in_list:
            if i in my_dict:
                value = my_dict[i]
                my_dict[i] = (value + dict_in_list[i])
            else:
                my_dict[i] = dict_in_list[i]
    return my_dict

