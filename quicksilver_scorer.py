# An implementation of the Quicksilver Scorer in Python
# Ported from:  http://code.google.com/p/rails-oceania/source/browse/lachiecox/qs_score/trunk/qs_score.js

import sets
import string

whitespace = sets.ImmutableSet(string.whitespace)

def qs(test_string, abbreviation, offset=None):
    offset = offset or 0

    if len(abbreviation) == 0: return 0.9
    if len(abbreviation) > len(test_string): return 0.0
    
    for i in xrange(len(abbreviation), 0, -1):
        sub_abbreviation = abbreviation[0:i]
        index = test_string.find(sub_abbreviation)
        
        if index < 0: continue
        if index+len(abbreviation) > len(test_string)+offset: continue
        
        next_string = test_string[index+len(sub_abbreviation)::]
        next_abbreviation = None
        
        if (i >= len(abbreviation)): next_abbreviation = ''
        else: next_abbreviation = abbreviation[i::]
        
        remaining_score = qs(next_string, next_abbreviation, offset+index)
        
        if remaining_score > 0:
            score = len(test_string)-len(next_string)
            
            if index != -1:
                j, c = 0, test_string[index-1]
                
                if c in whitespace:
                    for j in xrange(index-2, -1, -1):
                        c = test_string[j]
                        if c in whitespace: score = 1
                        else: score = 0.15
                else:
                    score -= index
            
            score += remaining_score*len(next_string)
            score /= len(test_string)
            
            return score
                
    return 0.0

print qs("hello world", "nothing is here")
print qs("hello world", "ow")
print qs("hello world", "helo")
print qs("hello world", "hello world")