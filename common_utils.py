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

def merge_list_to_dict(test_keys,test_values):
  """Using dictionary comprehension to merge two lists to dictionary"""
  merged_dict = {test_keys[i]: test_values[i] for i in range(len(test_keys))}
  return merged_dict

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

import os

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
def save_viz(VizName,plotvar,VizPath= None,dotsperinches = 600):
    if VizPath is None:
        ROOT_DIR = os.getcwd()
        VizPath = os.path.join(ROOT_DIR,"Visualizations")
    create_dir(VizPath,v=0)
    plotvar.savefig(os.path.join(VizPath,str(VizName)+'.png'),dpi=dotsperinches)

"""
Ignore Python Warnings
"""
import warnings
warnings.filterwarnings("ignore")
    
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
