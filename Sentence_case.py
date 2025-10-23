#Read the text from a file
with open('snowwhite.txt') as file:
    text = file.read() 

# Split the text into sentences based on ". "   

sentences = text.split(". ")

corrected_sentences = []

#Iterate through the list of sentences and correct the casing
for sentence in sentences:
    sentence = sentence.capitalize()
    corrected_sentences.append(sentence)


#Join the corrected sentences back into a single string
corrected_text = ". ".join(corrected_sentences)

#write the corrected sentences back to a new file
with open('snowwhite_corrected.txt', 'w') as file:
    file.write(corrected_text)