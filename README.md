<img width="1440" alt="Screenshot 2023-11-21 at 3 46 01 PM" src="https://github.com/Bereket32/Poetry-Slam/assets/145038776/73afa51e-26b6-442f-94fe-09e35ac58aea"># Poetry-Slam

Bereket Abebe

Bugs/issues: 
- issue with similarity method as it repeated sneds out strnig warning but can be disgarded. the scoring is consisent each run but was not able to figure out why
- Does not recite the audio file of poem but creates an audio file that contains gTTS saying the poem.
- also does not give option to save poem
- Now getting a type error with the audio file. Says I'm giving 2 arguements when there is only one input in the method.

Libraries used/ installations
- SpaCy
- pydantic
- gtts

How it works

Essentially takes in a trigger word that starts the poem off. Reads through an inspiring set of 1 poem and a bunch of drake songs and creates a bigram model of the words used from the inspiring set and words that frequently come after the words. a word is then chosen at random using the Random library and uses that word for the next word in the poem. The scoring is based on using a similarity method through spaCy with twos strings.

Have inlcuded sources at the top of the page of each class I used information I learned.
