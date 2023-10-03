from pathlib import Path
import os

# Empty Arrays that will be used to push files into
documents = []
pictures = []
music = []
videos = []
applications = []

# Get the download path file of the user
downloads_path = str(Path.home() / "Downloads")

# Ensure that the download path is pointing to the right place
print(downloads_path)

# Assign the files of the directory to a variable
list = os.listdir(downloads_path)

#Print out the current list of files in the download directory
print(list)


