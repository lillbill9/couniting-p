'''
Created on Feb 3, 2018

@author: ITAUser
'''
filename = "constituton.txt"
numberfile = open("constituton.txt", "r+");
'''text = numberfile.read();
words = text.split();
print(len(words));'''
num_words = 0
num_chars = 0
i = 0;
for line in numberfile:
    words = line.split()
    num_words = len(words)+ num_words
    for word in words:
        i += word.count("p")
        i += word.count("P")
print(i);
   
   