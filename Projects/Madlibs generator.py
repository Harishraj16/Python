with open("text.txt" , "r") as f:
    story = f.read()
    
words_in_para = set()
start_of_word = -1

target_start = "<"
target_end = ">"

#This locates all the words(to change) inside our story!

for i,char in enumerate(story):
    if char == target_start:
        start_of_word = i
        
    if char == target_end and start_of_word != -1:
        word = story[start_of_word : i+1]
        words_in_para.add(word)
        start_of_word = -1
        
        
#creating a dictionary to store the corrected words with the keys.
        
answers = {}

for word in words_in_para:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer
    
#Replacing the words
    
for word in words_in_para:
    story = story.replace(word, answers[word])
    
print(story)