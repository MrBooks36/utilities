from components.operations import *
from components.search import *
from sys import argv
from os import getcwd

def setpath(check):
 if check[0] == 'path':
   if len(check) > 1:
    path = check[1]
    print('Path Set To: '+path)
    return path
   else: print('Please Specify Path')
 else: return None

def count(check, path):
 if check[0] == 'count':
   if len(check) > 1:
    if check[1] == "files": print(str(countfiles(where=path)))+' files'
    elif check[1] =='folders': print(str(countfolders(where=path)))+' folders'   
    elif check[1] =='all':
     num = []
     num1 = str(countfiles(where=path))+' files'
     num2 = str(countfolders(where=path))+' folders'
     num.append(str(num1))
     num.append(str(num2))
     print(num)
   else: print('Please Specify Type')

def search(check, path):
 if check[0] == 'find':
   if not len(check) < 3:
    if check[1] == 'path': print(findpaths(pattern=check[2], where=path))
    elif check[1] == 'name': print(findname(pattern=check[2], where=path))
    elif check[1] == 'content': print(readall(pattern=check[2], where=path))
    elif check[1] == 'all':
     output = []
     output1 = str(readall(pattern=check[2], where=path))
     output2 = str(findpaths(pattern=check[2], where=path))
     output.append(output1)
     output.append(output2)
     print(output)
    else: print('Please Specify Search Item')
   else: print('Please Specify Search Item')

def rmemptyfolder(check, path):
 if check[0] == 'rmef': print(deleteallemptyfolders(where=path))

def delete(check, path):
 if check[0] == 'delete': print(deleteall(pattern=check[1], where=path))


def main():
 if len(argv) > 1:
  tokens = argv
  del tokens[0]
  opath = setpath(tokens)
  if opath:
   text = input('///')
   tokens = text.split()
  else: opath = getcwd() 
  count(tokens, opath)
  search(tokens, opath)
  delete(tokens, opath)
  rmemptyfolder(tokens, opath)
 else: print('Please Specify Command')



if __name__ == '__main__': main()