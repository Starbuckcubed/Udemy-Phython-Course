from datetime import datetime

today_notes = []

while True:
    line = input("Enter your notes for today. Type 'exit' to save and exit.")

    if line == 'exit':
        #breaks the loop, exit would break the program
        break
    today_notes.append(line)

#puts the items together with a new line in between each item
content = "\n".join(today_notes)

#extract the day of the week
day = datetime.now().strftime('%A')
filename = f'{day}.txt'
with open(filename, 'w') as file:
    file.write(content)

    print(f'Your notes have been saved to: {filename}')