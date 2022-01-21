"""
Common Utilities used in Day to Day Programming.
A Python Programmers Bread and Butter.
Author : Farhan Hai Khan
Github : @khanfarhan10
Original File at : https://github.com/khanfarhan10/custom_utils/
"""
def merge_list_to_dict(test_keys,test_values):
  """Using dictionary comprehension to merge two lists to dictionary"""
  merged_dict = {test_keys[i]: test_values[i] for i in range(len(test_keys))}
  return merged_dict

def sort_dict_elements_all(data, on_key = "confidence", reverse = True):
    list_of_keys = list(data.keys())
    list_of_values = list(data.values())
    item_index = list_of_keys.index(on_key)
    sorted_list_of_values = list(map(list, list(zip(*sorted(zip(*list_of_values), key=lambda sublist_to_sort_by: sublist_to_sort_by[item_index], reverse = reverse) ))))
    
    return merge_list_to_dict(test_keys = list_of_keys, test_values = sorted_list_of_values)
import os
def get_size(path = os.getcwd(), v= 0):
    """Get the Size of Folder/File, v = verbosity"""
    if v:
        print("Calculating Size: ",path)
    total_size = 0
    #if path is directory--
    if os.path.isdir(path):
      if v:
        print("Path type : Directory/Folder")
      for dirpath, dirnames, filenames in os.walk(path):
          for f in filenames:
              fp = os.path.join(dirpath, f)
              # skip if it is symbolic link
              if not os.path.islink(fp):
                  total_size += os.path.getsize(fp)
    #if path is a file---
    elif os.path.isfile(path):
      if v:
        print("Path type : File")
      total_size=os.path.getsize(path)
    else:
      if v:
        print("Path Type : Special File (Socket, FIFO, Device File)" )
      total_size=0
    bytesize=total_size
    if v:
        print(bytesize, 'bytes')
        print(bytesize/(1024), 'kilobytes')
        print(bytesize/(1024*1024), 'megabytes')
        print(bytesize/(1024*1024*1024), 'gegabytes')
    return total_size


x=get_size("/content/examples")

def props(img,show_uniques=True):
    print("Shape :",img.shape,"Maximum :",img.max(),"Minimum :",img.min(),"Data Type :",img.dtype)
    if show_uniques:
        print("Uniques :",np.unique(img))


import os, fnmatch
def find(pattern, path):
    """Utility to find files wrt a regex search"""
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result
FIND_FOLDER=os.getcwd()
zip_files=find('*.zip', FIND_FOLDER)

import os
import zipfile
import os
import shutil

def logger(*argv,logfile="log.txt",singleLine = False):
  """
  Writes Logs to LogFile
  """
  with open(logfile, 'a+') as f:
    for arg in argv:
      if type(arg) == dict:
        for key,val in arg.items():
          f.write(str(key) + " : "+ str(val))
          f.flush()
      else:
        f.write(str(arg))
        f.flush()
      if singleLine==False:
        f.write("\n")


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
"""
Download files with the help of ID from Google Drive
"""
!gdown --id yourFileIdHere


import matplotlib.pyplot as plt
%matplotlib inline
# helper function for data visualization
def visualize(**images):
    """PLot images in one row."""
    n = len(images)
    plt.figure(figsize=(20, 12))
    for i, (name, image) in enumerate(images.items()):
        plt.subplot(1, n, i + 1)
        plt.axis('off')
        plt.xticks([])
        plt.yticks([])
        plt.title(' '.join(name.split('_')).title())
        length = len(image.shape)
        if length==3:
            plt.imshow(image)
        else:
            plt.imshow(image,cmap="viridis")
    plt.show()
    
visualize(
    image=image, 
    building_mask=mask[..., 0].squeeze(),
    crops_mask=mask[..., 1].squeeze(),
    hill_mask=mask[...,2 ].squeeze(),
    # background_mask=mask[...,3 ].squeeze(),
)

import os
import zipfile
import shutil

#taken from : https://www.kaggle.com/xhlulu/recursion-2019-load-resize-and-save-images

def zip_and_remove(path):
    ziph = zipfile.ZipFile(f'{path}.zip', 'w', zipfile.ZIP_DEFLATED)
    
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            ziph.write(file_path)
            os.remove(file_path)
    
    ziph.close()
    shutil.rmtree(path)
    

for each_path in os.listdir("./"):
    if os.path.isdir(each_path):
        zip_and_remove(each_path)

CLASS_MAPPINGS = {v: k for k, v in CLASS_LABELLINGS.items()}
CLASS_MAPPINGS
def merge_list_to_dict(test_keys,test_values):
  """Using dictionary comprehension to merge two lists to dictionary"""
  merged_dict = {test_keys[i]: test_values[i] for i in range(len(test_keys))}
  return merged_dict

CLASSES = ['background','building','crops', 'hills']
VALUE_LABELS = list(range(len(CLASSES)))
CLASS_LABELLINGS = merge_list_to_dict(CLASSES,VALUE_LABELS)

import os
def advanced_listdir(direc):
    x = os.listdir(direc)
    new = []
    for e in x:
        new.append(os.path.join(direc,e))
    return new
ROOT_DIR = os.getcwd()
advanced_listdir(ROOT_DIR)
