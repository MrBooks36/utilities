def findall(pattern, where="c:/", output=False):
 import os
 import fnmatch
 if os.path.isfile(where):
  print('Not a folder: '+where)
 
 matches = []
 for root, dirnames, filenames in os.walk(where, topdown=False):
         for filename in fnmatch.filter(filenames, f'*{pattern}*'):
             matches.append(os.path.join(root, filename))
             for file in matches:
                if os.path.exists(os.path.join(root, file)) and output:
                 print(os.path.join(root, file))

 return matches

def findname(pattern, output=False, where="c:/"):
 import os
 import fnmatch
 if os.path.isfile(where):
  print('Not a folder: '+where)
 
 matches = []
 for root, dirnames, files in os.walk(where, topdown=False):
         for files in fnmatch.filter(files, f'*{pattern}*'):
             matches.append(files)
             for file in matches:
                if os.path.exists(os.path.join(root, file)) and output:
                 print(os.path.join(root, file))

 return matches

def readall(pattern, output=False, where="c:/"):
    import os
    import fnmatch  
    if os.path.isfile(where):
       print('Not a folder: '+where)
    matches = []
    for root, dirnames, filenames in os.walk(where, topdown=False):
         for filename in filenames:
                if os.path.exists(os.path.join(root, filename)):
                  try:
                   with open(os.path.join(root, filename), 'r') as file:
                     thing = file.read()
                     if fnmatch.fnmatch(str(thing), str(f'*{pattern}*')):
                       matches.append(os.path.join(root, filename))
                       file.close
                       if output:
                          print(thing)
                          file.close
                  except Exception as e:
                      if output:
                          print(e)   
                  if output:
                   print(os.path.join(root, filename))
    return matches

   
def countfiles(directory='c:/'):
    import os 
    if os.path.isfile(directory):
     print(f'Not a folder: '+directory)
    file_count = 0
    for root, dirs, files in os.walk(directory, topdown=False):
        file_count += len(files)
    return file_count

def countfolders(directory='c:/'):
    import os 
    if os.path.isfile(directory):
     print(f'Not a folder: '+directory)
    file_count = 0
    for root, dirs, files in os.walk(directory, topdown=False):
        file_count += len(files)
    return file_count