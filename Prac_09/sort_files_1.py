"""
Prac 09
Sort files to subdirectories based on extension
"""
import os


def main():
    """Move files into folders with the same name as their extension."""
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
