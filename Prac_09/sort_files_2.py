"""
Prac 09
Sort files to subdirectories based on extension and user chosen category
"""

import os


def main():
     """Move files into where user wants to store them based on extension."""

    #Dictionary to sort extensions into category folders
    extension_to_destination_folder = {}

    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        file_extension = filename.split('.')[-1]
        try:
            os.mkdir(file_extension)
        except FileExistsError:
            pass
        print("{}/{}".format(file_extension, filename))

        os.rename(filename, "{}/{}".format(file_extension, filename))


main()

