#main method 
from Evaluation import Evaluation
from Creation import Creation
from Voice import Voice
class Generation():
    
    def reading(file):
        with open(file, "r") as files:
            lines = files.readlines()
            print(lines)
            print()
        
def main():
    tester = Evaluation()
    
    Audio = Voice()
    
    
    file = Creation.reading("Inspiring_set.txt")
    predictor = Creation(file)


    Emp_txt = open('created_poem.txt', 'w')
    #input word
    #question = input("what word word you like")
    #For some reasons input's won't work for the current word. Labeling error through this comment 
    current_word = "i"
    counter = -1
    Emp_txt.write(current_word)


    '''Length of Poem set at 200 and using the the current word to start of the poem we enter the loop. The counter variable simply 
     validates line compacity at a length of 7 befroe it starts a new line'''
    for i in range(200):#range(len(file)):
        counter = counter + 1
        predicted_next_word = predictor.predict_next_word(current_word)

        if predicted_next_word == "Help":
            predicted_next_word = "$"
            if counter % 7 == 0:
                Emp_txt.write(predicted_next_word + " " + '\n')
 
            else:
                Emp_txt.write(predicted_next_word + " ")

        else:
            if counter % 7 == 0:
                Emp_txt.write(predicted_next_word + " " + '\n')

            else:
                Emp_txt.write(predicted_next_word + " ")
                current_word = predicted_next_word
                #counter + 1
        
    Emp_txt.close()
    
    
    #scoring 
    print(tester.similarity('tester.txt','created_poem.txt'))
    
    #Creating audio file Error here too. Can't figure out why. Keeps saying I'm giving 2 arguements when I'm very clearly giving 2
    Audio.speaking("created_poem.txt")
    

if __name__ == "__main__":
    main()

