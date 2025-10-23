import os
import dropbox
import dotenv

dotenv.load_dotenv()
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

d = dropbox.Dropbox(ACCESS_TOKEN)

folder_path = "files"

#gets a list of all files in a directory- you have to reverse the slashes
#dir_list = os.listdir(path)
#print("Files and directories in '", path, "' :")
# prints all files
#print(dir_list)

## Iterate through all files in the directory
for filename in os.listdir(folder_path):
    # Build the full local file path
    full_file_path = os.path.join(folder_path, filename)

    # Check if it's a file (not a directory)
    if os.path.isfile(full_file_path):
        with open(full_file_path, 'rb') as file:
            content = file.read()
            # Upload to Dropbox with the same filename
            dropbox_path = f'/{filename}'
            d.files_upload(content, dropbox_path, mode=dropbox.files.WriteMode('overwrite'))
            print(f'File {filename} uploaded successfully!')

#found the path using current_directory = os.getcwd()
#print(f"Current working directory: {current_directory}")
# C:\Users\gguillor\Documents\Udemy_Phython_Course\Lesson 9