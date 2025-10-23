import glob

#sorts files
filepaths = sorted(glob.glob('text_files/*.txt'))

#needs to be declared before the for loop
word_counter ={}


for filepath in filepaths:
    with open(filepath, 'r') as file:
        #creates a string
        content=file.read()
        # string method applied which allows us to treat each word as a separate object
        words = content.split()

        for word in words:
            #if the word hasn't been counted yet then set it equal to 1
            if not word in word_counter:
                word_counter[word] = 1
            #if the word has been counted, and it comes up again add 1 to it's count
            else:
                word_counter[word] += 1

print(word_counter)

with open('word_frequencies.txt', 'w') as file:
    #access each key and value
    for word, count in word_counter.items():
        file.write(f'{word}: {count}\n')