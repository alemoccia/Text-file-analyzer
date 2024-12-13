# Project #1 - Text file analyzer 13/12/2024

# Aim of this project: 
# Write a program capable of reading any .txt file and providing: 
# Word count, Line count and Frequency of each word (NOT case sensitive)

word_count = 0
line_count = 0
word_frequency = {}

filename = "spider.txt"


with open(filename, "r") as file:       # Opens up the file in read mode
    for line in file:

        words = line.split()            # Splits each line into its own list of words 
    
        for word in words: 
            word_count += 1

            if word in word_frequency:
                word_frequency[word] += 1   
            else:
                word_frequency[word] = 1
                
         
        line_count += 1


print("The file {} contains {} words".format(filename, word_count))
print("The file {} contains {} lines".format(filename, line_count))

for key, value in word_frequency.items():
    print(f"{key}: {value}")




