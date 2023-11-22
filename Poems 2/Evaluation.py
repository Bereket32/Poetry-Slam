#Sources
#https://spacy.io/usage/linguistic-features
import spacy
from Creation import Creation


class Evaluation():
    
    
    def __init__(self):
        self.cool = 0
  
  
    def similarity(self, text1, text2):
        ''' Compares the similarity between two different txt files and returns a score of similarity'''
        nlp = spacy.load('en_core_web_sm')
        compare1 = nlp(' '.join(text1))
        compare2 = nlp(' '.join(text2))
        return compare1.similarity(compare2)

 
    