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
doc = ('.doc', '.docx', '.txt', '.pdf','.txt', 'ppt')
pic = ('.img', '.jpg', ".jpeg", ".png")
aud = ('.mp3', '.wav', '.flac')
vid = ('.mkv', '.mp4', '.webm', '.mov', '.avi', '.m4v','.gif')
apps = ('.exe','msi', '.cap')

# Get the default file paths of the user
downloads_path = str(Path.home() / "Downloads")
documents_path = str(Path.home() / "Documents")
pictures_path = str(Path.home() / "Pictures")
music_path = str(Path.home() / "Music")
videos_path = str(Path.home() / "Videos")

# Need to create a new folder for applications in the user folder and that is what will hold the users applications



# Ensure that the download path is pointing to the right place
# print(downloads_path)

# Assign the files of the directory to a variable
list = os.listdir(downloads_path)

#Print out the current list of files in the download directory
# print(list)

# write a function to append files that end with doc extenion to the documents list
def documentsAppend():
    for files in list:
        if files.endswith(doc):
            docFiles = files
            documents.append(docFiles)
    print(len(documents))

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

# write a function to append files that end with aud extenion to the music list
def musicAppend():
    for files in list:
        if files.endswith(aud):
            audFiles = files
            music.append(audFiles)
    print(len(music))
            
# write a function to append files that end with apps extenion to the application list
def applicationsAppend():
    for files in list:
        if files.endswith(apps):
            appFiles = files
            applications.append(appFiles)
    print(len(applications))

documentsAppend()
picturesAppend()
musicAppend()
videosAppend()
applicationsAppend()

         
