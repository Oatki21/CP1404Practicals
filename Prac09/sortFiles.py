"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import os
import shutil

__author__ = 'Lindsay Ward'

print("Current directory is", os.getcwd())

# change to desired directory
os.chdir('FilesToSort')
# print a list of all files (test)
print(os.listdir('.'))
extensions = ["xlsx", "xls", "txt", "png", "jpg", "gif", "docx", "doc"]
for extension in extensions:
    os.mkdir('{}'.format(extension))

os.chdir('.')
for dir_name, subdir_list, file_list in os.walk('.'):
    # print("In", dir_name)
    # print("\tcontains subdirectories:", subdir_list)
    # print("\tand files:", file_list)
    for filename in file_list:
        for extension in extensions:
            if os.path.splitext(filename)[1] == ".{}".format(extension):
                shutil.move(filename, '{}/'.format(extension))
