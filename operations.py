def deleteall(pattern, where="c:/", output=False):
   import os
   import fnmatch
 
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