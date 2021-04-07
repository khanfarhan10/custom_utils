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
    
def getExtension(filepath):
  """Returns the extension of the given filepath"""
  complete_filename, file_extension = os.path.splitext(filepath)
  return file_extension

def countExtensions(ListofPaths):
  """Returns a dictionary of element counts present in the directory"""
  files = dict()
  for each in ListofPaths:
    extension = getExtension(each)
    if extension not in files:
      files[extension]=1
    else:
      files[extension]=files[extension]+1
  return files
"""
Usage :
countExtensions(ListofPaths=os.listdir(cvd))
"""


import os
def get_size(path = os.getcwd()):
    """Get the Size of Folder/File"""
    print("Calculating Size: ",path)
    total_size = 0
    #if path is directory--
    if os.path.isdir(path):
      print("Path type : Directory/Folder")
      for dirpath, dirnames, filenames in os.walk(path):
          for f in filenames:
              fp = os.path.join(dirpath, f)
              # skip if it is symbolic link
              if not os.path.islink(fp):
                  total_size += os.path.getsize(fp)
    #if path is a file---
    elif os.path.isfile(path):
      print("Path type : File")
      total_size=os.path.getsize(path)
    else:
      print("Path Type : Special File (Socket, FIFO, Device File)" )
      total_size=0
    bytesize=total_size
    print(bytesize, 'bytes')
    print(bytesize/(1024), 'kilobytes')
    print(bytesize/(1024*1024), 'megabytes')
    print(bytesize/(1024*1024*1024), 'gegabytes')
    return total_size


x=get_size("/content/examples")

"""
Kaggle Datasets Download in Colab:
!pip install kaggle

import os
os.makedirs("/content/.kaggle/")

import json
token = {"username":"farhanhaikhan","key":"f2c0df223af325f0d811a0f18b0c02ca"}
with open('/content/.kaggle/kaggle.json', 'a+') as file:
    json.dump(token, file)

import shutil
os.makedirs("/.kaggle/")
src="/content/.kaggle/kaggle.json"
des="/.kaggle/kaggle.json"
shutil.copy(src,des)


os.makedirs("/root/.kaggle/")
!cp /content/.kaggle/kaggle.json ~/.kaggle/kaggle.json

!kaggle config set -n path -v /content

#https://towardsdatascience.com/setting-up-kaggle-in-google-colab-ebb281b61463

!kaggle competitions download -c digit-recognizer

!kaggle datasets download -d tawsifurrahman/covid19-radiography-database

!unzip -q covid19-radiography-database.zip -d /content/dataset

src="/content/Dataset.zip"
des="/content/DATA/"
get_ipython().system('unzip -q {} -d {}'.format(src,des))
"""

"""
Ignore Python Warnings
"""
import warnings
warnings.filterwarnings("ignore")
    
"""
Utility for Compressing Directories to .zip file
zipper('/content/MAIN/Train', "Zipped_Data.zip")
"""


import os
import zipfile
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


def zipper(dir_path, zip_path):
    zipf = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)
    zipdir(dir_path, zipf)
    zipf.close()

"""
Mount Google Drive
"""
from google.colab import drive
drive.mount('/content/drive')
