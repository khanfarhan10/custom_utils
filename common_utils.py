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
