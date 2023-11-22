#https://spacy.io/usage/linguistic-features
import spacy
from Creation import Creation


class Evaluation():
    
    
    
    def __init__(self):
        self.cool = 0
  
    
    
    def similarity(self, text1, text2):
        nlp = spacy.load('en_core_web_sm')
        compare1 = nlp(' '.join(text1))
        compare2 = nlp(' '.join(text2))
        return compare1.similarity(compare2)
      
def main():
    tester = Evaluation()
    
    tester.similarity('tester.txt','created_poem.txt')
    print("ok")
      
    
if __name__ == "__main__":
    main()
    
 
    