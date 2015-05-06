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

    return temp


# Decorator called sycnronized that uses threading to synchroznise access
def synchronized(func):
    func.__lock__ = threading.Lock()
    def synced_func(*args, **kws):
        with func.__lock__:
            return func(*args, **kws)
    return synced_func



if __name__ == "__main__":
    s = '''A]le.ksey', ; K:@$%^&*rame()_+r 12345     67890
    asfasdfa


    elskey

    *()(70979u685ngobbt978qiuw@!@#$%^&kjkladf)   


    Alek;s&ey'''
    print(s)
    print(clean(s))
