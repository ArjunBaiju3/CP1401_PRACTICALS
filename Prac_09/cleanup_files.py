"""
CP1404/CP5632 Practical
Cleanup song file names
"""

import os


def main():
    """Cleanup or alter song filenames to same format"""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' format of filename."""
    filename_with_underscore = filename.replace(" ", "_").replace(".TXT", ".txt").strip(".txt")
    if "_" not in filename_with_underscore:  # if filename is not separated
        separated_filename = "".join(" " + char if char.isupper() else char for char in filename_with_underscore).strip(
            " ").split(" ")
        formatted_filename = "_".join(separated_filename)
    else:
        formatted_filename = filename_with_underscore.title()
    return formatted_filename + ".txt"


main()
