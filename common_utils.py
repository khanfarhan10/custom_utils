"""
Common Utilities used in Day to Day Programming.
A Python Programmers Bread and Butter.
Author : Farhan Hai Khan
Github : @khanfarhan10
Original File at : https://github.com/khanfarhan10/custom_utils/
"""

def create_dir(dir,v = 1):
  """Creates a directory without throwing an error if directory already exists.
  dir : The directory to be created.
  v : Verbosity"""
  if not os.path.exists(dir):
    os.makedirs(dir)
    if v:
      print("Created Directory : ", dir)
    return 1
  else:
    if v:
      print("Directory already existed : ", dir)
    return 0
  
