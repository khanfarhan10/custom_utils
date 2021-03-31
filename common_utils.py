"""
Common Utilities used in Day to Day Programming.
A Python Programmers Bread and Butter.
Author : Farhan Hai Khan
Github : @khanfarhan10
Original File at : https://github.com/khanfarhan10/custom_utils/
"""
import os
import zipfile
import os
import shutil


def create_dir(dir, v=1):
    """
    Creates a directory without throwing an error if directory already exists.
    dir : The directory to be created.
    v : Verbosity
    """
    if not os.path.exists(dir):
        os.makedirs(dir)
        if v:
            print("Created Directory : ", dir)
        return 1
    else:
        if v:
            print("Directory already existed : ", dir)
        return 0


def DeleteFolderContents(dir):
    """Delete the contents of a folder without deleting the folder itself"""
    create_dir(dir)
    shutil.rmtree(dir)
    create_dir(dir)

def print_list(lst):
  """ Pretty Fancy way to print a list"""
  for e in lst:
    print(e)

def getBaseNameNoExt(givenPath):
    """Returns the basename of the file without the extension"""
    filename = os.path.splitext(os.path.basename(givenPath))[0]
    return filename
def subtract_lists(x,y):
    """Subtract Two Lists (List Difference)"""
    return [item for item in x if item not in y]

"""
Utility for Compressing Directories to .zip file
zipper('/content/MAIN/Train', "Zipped_Data.zip")
"""


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


def zipper(dir_path, zip_path):
    zipf = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)
    zipdir(dir_path, zipf)
    zipf.close()
