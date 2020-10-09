from pathlib import Path
from zipfile import ZipFile

# Chapter 9.5- Working with Zip files
print("\nChapter 9.5- Working with Zip files " + "-" * 20)
# requires "from zipfile import ZipFile" see line 32
# I modified Mosh's code to make zipping more reusable
# you can change these three variables for your future needs
# If the zip file exists, this code will overwrite the existing zip file
