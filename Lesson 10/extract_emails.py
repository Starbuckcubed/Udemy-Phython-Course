import os
# regular expressions
import re
directory ='Emails'

filenames = os.listdir(directory)

all_emails = []

for filename in filenames:
    #had to create the filepath because the python file is not in the same directory as the email files
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r') as file:
        content = file.read()

#recommended by copilot
    #emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', content)
    #recommended by course
    #looks for any character a-z, A-Z, 0-9, ., _, %, +, - followed by @ followed by any character a-z, A-Z, 0-9, ., - followed by . followed by at least two characters a-z or A-Z
    pattern= r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    #findall returns a list of all matches
    emails = re.findall(pattern, content)
    #extend method gets the items of a list and puts them in another list
    all_emails.extend(emails)

print(all_emails)