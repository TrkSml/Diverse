"""

This is a Dictionary-based Analyzer/Reviewer based on Levenshtein distance. 
All you have to do first is define a dictionary (list/array) . Any word you type in will be matched with the most approximate
item contained within the dictionary .

"""
import numpy as np

def lev(source, target):
    if len(source) < len(target):
        return lev(target, source)

    if len(target) == 0:
        return len(source)

    source = np.array(tuple(source))
    target = np.array(tuple(target))

    previous_row = np.arange(target.size + 1)
    for s in source:
        current_row = previous_row + 1

        current_row[1:] = np.minimum(
                current_row[1:],
                np.add(previous_row[:-1], target != s))

        current_row[1:] = np.minimum(
                current_row[1:],
                current_row[0:-1] + 1)

        previous_row = current_row

    return previous_row[-1]

class Dictionary:
    def __init__(self,words):
        self.words=words
        
    def find_most_similar(self,term):
      minimum=min([lev(term,c) for c in self.words])
      return self.words[[minimum==lev(term,c) for c in self.words].index(True)]
        
