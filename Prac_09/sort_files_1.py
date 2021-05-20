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



main()
