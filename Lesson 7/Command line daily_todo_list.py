from datetime import datetime

todo_items = []

while True:
    todo = input("Enter your to-do lists items for today. Type 'done' to save and exit.")

    if todo == 'done':
        #breaks the loop, exit would break the program
        break
    todo_items.append(todo)

#puts the items together with a new line in between each item
content = "\n".join(todo_items)

#extract the day of the week
day = datetime.now().strftime('%A')
filename = f'{day}.txt'
with open(filename, 'w') as file:
    file.write(content)

    print(f'Your to do list file written to: {filename}')
