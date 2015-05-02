import threading
import re
import string

# character sets allowed in the string
chars = string.ascii_letters + string.digits + string.whitespace + string.punctuation



# Function to strip all but ascii letters, digits, and whitespace
def asciiextractor(inString, allowed_list=chars):
    # Isolate ascii chars only
    temp = "".join([ch for ch in inString if ch in allowed_list])
    
    # remove punctuation. # make sure to use str() to get rid of unicode
    replace_punctuation = string.maketrans(string.punctuation, ' ' * len(string.punctuation))
    temp = str(temp).translate(replace_punctuation)

    return temp


# Decorator called sycnronized that uses threading to synchroznise access
def synchronized(func):
    func.__lock__ = threading.Lock()
    def synced_func(*args, **kws):
        with func.__lock__:
            return func(*args, **kws)
    return synced_func

if __name__ == "__main__":
    s = "A]le.ksey', ; K:@$%^&*rame()_+r 12345     67890\n"
    print(asciiextractor(s))
