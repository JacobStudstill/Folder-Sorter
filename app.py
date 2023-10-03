from pathlib import Path
import os

# Empty Arrays that will be used to push files into
documents = []
pictures = []
music = []
videos = []
applications = []
other = []

#define extension types
doc = ('.doc', '.docx', '.txt', '.pdf')
pic = ('.img', '.jpg', ".jpeg", ".png")
vid = ('mkv', 'mp4', 'webm', 'mov', 'avi', 'm4v')
aud = ('mp3', 'wav', 'flac')

# Get the download path file of the user
downloads_path = str(Path.home() / "Downloads")

# Ensure that the download path is pointing to the right place
# print(downloads_path)

# Assign the files of the directory to a variable
list = os.listdir(downloads_path)

#Print out the current list of files in the download directory
print(list)

# write a function to append files that end with pic extenion to the pictures list
def picturesAppend():
    for files in list:
        if files.endswith(pic):
            picFiles = files
            pictures.append(picFiles)
    print(len(pictures))

# write a function to append files that end with pic extenion to the videos list
def videosAppend():
    for files in list:
        if files.endswith(vid):
            vidFiles = files
            videos.append(vidFiles)
    print(len(videos))

# write a function to append files that end with doc extenion to the documents list
def documentsAppend():
    for files in list:
        if files.endswith(doc):
            docFiles = files
            documents.append(docFiles)
    print(len(documents))

            

picturesAppend()
videosAppend()
documentsAppend()
         
