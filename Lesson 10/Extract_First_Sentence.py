import os
# regular expressions
import re
directory = 'sentences'
# Ensure the 'sentences' directory exists
if not os.path.isdir(directory):
    raise FileNotFoundError(f"The directory '{directory}' does not exist.")
all_first_sentences = []

# Loop through all files in the directory
for filename in os.listdir(directory):
    #had to create the filepath because the python file is not in the same directory as the text files
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r') as file:
        content = file.read()

       # Use regular expression to find all sentences
    pattern = r'[A-Za-z0-9,;"\'\s\-()]+[.!?]'
    first_sentences = re.findall(pattern, content)

     # Add the first sentence from the match to the list if available
    if first_sentences:
        all_first_sentences.append(first_sentences[0])

# Print all first sentences one per line
for sentence in all_first_sentences:
    print(sentence)