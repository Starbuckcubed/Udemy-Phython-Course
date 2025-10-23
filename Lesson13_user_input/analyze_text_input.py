from string import punctuation

#function to remove the punctuation from the text and replace with empty string
def remove_punctuation(text):
    punctuation = ".,!?()[]{}"
    for char in punctuation:
        text = text.replace(char, '')
        return text

text = input("Enter a block of text for analysis\n")
characters = len(text)
words = len(text.split())
sentences = text.count(".") + text.count("!")+text.count("?")

word_frequency = {}
wordlist= remove_punctuation(text).lower().split()
#iterate through words if the word is in not in the list count is as one if it is added 1 to it's number
for word in wordlist:
    if not word in word_frequency:
        word_frequency[word] = 1
    else:
        word_frequency[word] += 1
# the get makes sure you get the highest because otherwise it would give you the first in the alphabet
most_frequent_word = max(word_frequency, key=word_frequency.get)

#list of lenghts of words
#calculate
lengths = [len(word) for word in wordlist]
average_word_length = sum(lengths) / (len(lengths))
average_sentence_length = words / sentences

print(word_frequency)
print("Text Analysis Results:")
#formatting to separate title from the results
print("-" * 25)
# f string allows us to enter a literal string & a variable in the curly brackets
print(f"Total character: {characters}")
print(f"Total Words: {words}")
print(f"Total sentences: {sentences}")
print(f"Most frequent word: '{most_frequent_word}' (used {word_frequency[most_frequent_word]} times)")
print(f"Average word length: {average_word_length}")
print(f"Average sentence length: {average_sentence_length} words")