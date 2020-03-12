import os
def list_files(directory, min_file_size):
    files = [ ]
    for root, dirs, files in os.walk(directory):
            for name in files:
                    filename = os.path.join(root, name)
                    if os.stat(filename).st_size > min_file_size:
                            files.append(filename)
    return files


print(list_files("C:/Users/51DOS/Desktop/Test Folder", 20))
