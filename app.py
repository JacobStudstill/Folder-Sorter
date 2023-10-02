from pathlib import Path
import os

downloads_path = str(Path.home() / "Downloads")
list = os.listdir(downloads_path)

# open(downloads_path)

# print (downloads_path.readable())