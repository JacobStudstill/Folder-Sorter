from pathlib import Path
import os
import shutil

# Empty Arrays that will be used to push files into
documents = []
pictures = []
music = []
videos = []
applications = []
other = []

#define extension types
doc = ('.doc', '.docx', '.txt', '.pdf','.txt', 'ppt')
pic = ('.img', '.jpg', '.jpeg', '.png','webp')
aud = ('.mp3', '.wav', '.flac')
vid = ('.mkv', '.mp4', '.webm', '.mov', '.avi', '.m4v','.gif')
apps = ('.exe','msi', '.cap')

# Get the default file paths of the user
parent_path = str(Path.home())
downloads_path = str(Path.home() / "Downloads")
documents_path = str(Path.home() / "Documents")
pictures_path = str(Path.home() / "Pictures")
music_path = str(Path.home() / "Music")
videos_path = str(Path.home() / "Videos")

# Need to create a new folder for applications in the user folder and that is what will hold the users applications

# Assign the files of the directory to a variable
list = os.listdir(downloads_path)

# write a function to append files that end with doc extenion to the documents list
def documentsAppend():
    for files in list:
        if files.endswith(doc):
            documentFinal = os.path.join(downloads_path, files)
            shutil.move(documentFinal, documents_path)
            #Create a txt file in downloads folder that will hold the file names for files moved to new folder
    print("Documents have been moved to Documents Folder")

# write a function to append files that end with pic extenion to the pictures list
def picturesAppend():
    for files in list:
        if files.endswith(pic):
           picFinal = os.path.join(downloads_path, files)
           shutil.move(picFinal, pictures_path)
    print("Pictures have been moved to Documents Folder")

# write a function to append files that end with pic extenion to the videos list
def videosAppend():
    for files in list:
        if files.endswith(vid):
            vidFinal = os.path.join(downloads_path, files)
            shutil.move(vidFinal, videos_path)
    print("Videos have been moved to Videos Folder")

# write a function to append files that end with aud extenion to the music list
def musicAppend():
    for files in list:
        if files.endswith(aud):
            audFinal = os.path.join(downloads_path, files)
            shutil.move(audFinal, music_path)
    print("Music have been moved to Music Folder")
            
# write a function to append files that end with apps extenion to the application list
def applicationsAppend():
    for files in list:
        if files.endswith(apps):
            appFiles = files
            applications.append(appFiles)
    print(len(applications))

# ask user if they want to add a folder for coding files
def codingFile():
    answer = input("Would you like to add a folder for coding files? ")
    answer.lower()
    match answer:
        case "yes":
            folder_name = input ("What do you want your folder to be named?")
            print("A folder will be created for your program files")

        case "no":
            print("A folder will not be created for your program files")
        case _:
            print("Invalid answer, please try again")
            codingFile()

codingFile()
documentsAppend()
picturesAppend()
musicAppend()
videosAppend()
applicationsAppend()
