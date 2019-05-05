#Import the classes
import os

#read the file as text_file and store it in paragraph
text_file = open("paragraph_0.txt")
paragraph = text_file.read()

#calc the lines using ". " as a seperator
lines = paragraph.split('. ')
approximate_sentence_count = len(lines)

#calc the words using " " as a seperator
words = paragraph.split(' ')
approximate_word_count = len(words)

#find the total letters
total_letter_count = 0
for i in words:
    total_letter_count += len(i)

#calc and print the results

print ("---------------------------------")
print ("Paragraph Analysis")
print ("---------------------------------")
print ("Approximate Word Count: ", approximate_word_count)
print ("Approximate Sentence Count: ", approximate_sentence_count)
print ("Average Letter Count: ", round(total_letter_count/approximate_word_count,1))
print ("Average Sentence Length: ", approximate_word_count/approximate_sentence_count)
print ("---------------------------------")

text_file.close()