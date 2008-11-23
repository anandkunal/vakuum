# A poor man's anagram implementation

import collections
import sets
import string

# Static set will be used to avoid whitespace, digits, and punctuation
english_letters = sets.ImmutableSet(string.ascii_letters)

def is_anagram(str1=None, str2=None):
    # Using a defaultdict of type 'int' is useful for counters
    discovered_letters = collections.defaultdict(int)
    
    if (str1 and str2 and (type(str1) is str) and (type(str2) is str)):
        # Lowercase everything once - don't do it in the for loops N times
        str1, str2 = str1.lower(), str2.lower()
        # Load the discovered letters
        for char in str1:
            if (char in english_letters):
                discovered_letters[char] += 1
        # Go through the second string
        for char in str2:
            if (char in english_letters):
                if char in discovered_letters:
                    discovered_letters[char] -= 1
                    if (discovered_letters[char] == 0):
                        del discovered_letters[char]
                else:
                    return False
        # Check the length
        if (len(discovered_letters)):
            return False
        return True
    else:
        # Raise an argument exception here
        raise ValueError, "Badness - input arguments must be strings"

# I found these test cases online at: http://www.entisoft.com/ESTools/StringWords_IsAnagram.HTML
print is_anagram("abba", "baba")
print is_anagram("Tim Taylor", "Mortality")
print is_anagram("Jill Taylor", "Jolly Trail")
print is_anagram("Hello World", "This is a test.")

# I found these test cases at Wikipedia: http://en.wikipedia.org/wiki/Anagram
# Some of them are out of control!
print is_anagram("Gregory House", "Huge ego, sorry")
print is_anagram("Hillary Diane Rodham Clinton", "Tally ho! Iron-handed criminal")
print is_anagram("Clint Eastwood", "Old West action")

# These should be obvious failures
print is_anagram("fjdsklfdsf", "fjadsfljsadklfas")
print is_anagram("as", "a")
