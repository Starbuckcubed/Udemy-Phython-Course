import os

# Create a new folder named 'new_folder' in the current directory if it doesn't exist

for item in os.listdir():
    if os.path.isdir(item) and item.isdigit():
        new_name = f"lesson_{item}"
        os.rename(item, new_name)
        print(f"Renamed folder '{item}' to '{new_name}'.")
