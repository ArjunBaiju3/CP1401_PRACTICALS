"""
Prac 09
Sort files to subdirectories based on extension and user chosen category
"""

import os


def main():
    """Move files into user inputted directory"""
    # Dictionary to sort extensions into category folders
    extension_to_destination_folder = {}

    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        file_extension = filename.split('.')[-1]
        if file_extension not in extension_to_destination_folder:
            category = input("What category would you like to sort {} files into? ".format(file_extension))
            extension_to_destination_folder[file_extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass

        os.rename(filename, "{}/{}".format(extension_to_destination_folder[file_extension], filename))


main()
