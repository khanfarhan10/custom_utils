
import os
import csv

path = os.getcwd() 

def getExtension(filepath):
  complete_filename, file_extension = os.path.splitext(filepath)
  return file_extension

columns=['FileName','FileExtension','AbsolutePath','FolderName']

with open('indexed_file.csv', mode='w') as fh:
  fwriter = csv.writer(fh, delimiter=',')
  fwriter.writerow(columns)
  for root, _ , files in os.walk(path):
      files = [f for f in files if not f.startswith('~') and f!='Thumbs.db']
      paths = [os.path.join(root,f) for f in files]
      extensions = [getExtension(f) for f in files]
      foldernames = [os.path.dirname(p) for p in paths]



      for fname,fext,abspth,folname in zip(files,extensions,paths,foldernames):
        fwriter.writerow([str(fname),str(fext),str(abspth),str(folname)])
