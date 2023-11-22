from pydantic import FilePath
import spacy
import os
import random

#https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-language-model-nlp-python-code/
#https://datachild.net/machinelearning/bigram-language-model-python


class Creation:
        
    def __init__(self, text):
        self.nlp = spacy.load("en_core_web_sm")
        self.bigram_model = self.build_bigram_model(text.lower())
        
    def reading(file):
        with open(file, 'r') as file:
            data = file.read()
        return data
        
    def build_bigram_model(self, text):
        Emergency_word = "Help"
        doc = self.nlp(text)
        bigrams_list = []
        for i in range(len(doc) - 1):
            cur_word = doc[i]
            next_word = doc[i + 1]
            bigrams_list.append((cur_word.text, next_word.text))
        return Creation.bigram_helper(bigrams_list)
        

    def bigram_helper(list):
        frequecy = {}
        for word in list:
            frequecy.setdefault(word[0], []).append(word[1])
        return frequecy
        
   
    def predict_next_word(self, current_word):
        if current_word in self.bigram_model:
            next_word_options = self.bigram_model[current_word]
            return random.choice(next_word_options)
        else:
            Emergency_word = "Help"
            return Emergency_word
    
        
        #check if we should reach the end of a line and start a new one
        return
        
def main():
  
    file = Creation.reading("Inspiring_set.txt")

    #print(file)
    # Example usage
    #corpus = "Harrison likes to hop and jump with John really fast but now she fell so she is unhappy. Jummping is an activity that we don't really talk about. Playing soccer is nice too if we actually play"

    #predictor = Creation(corpus)
    predictor = Creation(file)


    # predicted_next_word = predictor.predict_next_word(current_word)
    # print(predicted_next_word)

    Emp_txt = open('created_poem.txt', 'w')
    current_word = "i"
    emp_string = ""
    counter = -1
    Emp_txt.write(current_word)



    for i in range(200):#range(len(file)):
        counter = counter + 1
        predicted_next_word = predictor.predict_next_word(current_word)
        emp_string = predicted_next_word
        if predicted_next_word == "wrong":
            predicted_next_word = "$"
            if counter % 7 == 0:
                Emp_txt.write(predicted_next_word + " " + '\n')
                #counter + 1
            else:
                Emp_txt.write(predicted_next_word + " ")
                #counter + 1
        else:
            if counter % 7 == 0:
                Emp_txt.write(predicted_next_word + " " + '\n')
                #counter + 1
            else:
                Emp_txt.write(predicted_next_word + " ")
                current_word = predicted_next_word
                #counter + 1
        
    Emp_txt.close()








    #print("We green")
    #line = "Harrison likes to hop and jump with John really fast but now she fell so she is unhappy."
    #Creation.sentence_analyzer(line)

if __name__ == "__main__":
    main()
    
    