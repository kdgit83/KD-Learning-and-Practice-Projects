import os

def file_info():
    # Your code goes here.
    total_bytes = 0
    folder_name = "deps"
    folder_path = os.path.realpath(folder_name)
    if os.path.exists(folder_path):
        contents = os.listdir(folder_path)
        for item in contents:
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path) and item.endswith('txt'):
                file_size = os.path.getsize(item_path)
                total_bytes += file_size
    return total_bytes

print("Total byte count of the text files under deps folder: ", file_info())
