def deleteall(pattern, where="c:/", output=False):
   import os
   import fnmatch
   if os.path.isfile(where):
       raise Exception(f'Not a folder: {where}')
 
   matches = []
   for root, dirnames, files in os.walk(where, topdown=False):
         for filename in fnmatch.filter(files, f'*{pattern}*'):
             matches.append(filename)
             for file in matches:
                if os.path.exists(os.path.join(root, file)):
                 try:
                  os.remove(os.path.join(root, file))
                 except Exception as e:
                    if output:
                       print(e)
                 if output:
                  print('deleted: ' + os.path.join(root, file))
   return matches

def deletemptyfolders(where="c:/", output=False):
    import os
    import fnmatch
    if os.path.isfile(where):
       raise Exception(f'Not a folder: {where}')
    matches = []
    for root, dirs, files in os.walk(where, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            try:
             if not fnmatch.fnmatch(dir_path, "*Application Data*"):
              if not os.listdir(dir_path) and not fnmatch.fnmatch(dir_path, "*AppData/LocalLow/Microsoft*") and not fnmatch.fnmatch(dir_path, "*AppData/Local/Microsoft*"):  # Check if the directory is empty
                os.rmdir(dir_path)
                if output:
                 print(f"Deleted empty folder: {dir_path}")
                 matches.append(dir_path)
            except Exception as e:
                  if output:
                   print(e)
    return matches

def deleteallemptyfolders(where="c:/", output=False):
 while deletemptyfolders(where=where, output=output):
  if output:
   print(True)