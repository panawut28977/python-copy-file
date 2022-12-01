import os
import shutil
import csv

# Execute Step
# 1. Change parent_folder to your parent_folder. Parent folder would be a starting point of searching.
# 2. Change destination folder to where you want the files to go.
# 3. Update searching text in csv file. The program will compare searching texts with all files under parent folder.

parent_folder = "/Users/panawut.i/code/copy-file"
destination_folder = "/Users/panawut.i/code/copy-file/destination"

# Get list of search text
list_of_search_text = []
file = open('search-text.csv')
csvreader = csv.reader(file)
for row in csvreader:
        list_of_search_text.append(row)
file.close()

#Find file
list_of_file = []
for (root,dirs,files) in os.walk(parent_folder, topdown=True):
    for file_name in files:
        for search_text in list_of_search_text:
            if search_text[0] in file_name.lower():
                list_of_file.append(os.path.join(root, file_name))

#copying file to destination folder
for src in list_of_file:
    shutil.copy(src,destination_folder)
