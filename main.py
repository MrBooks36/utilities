from components.operations import deleteallemptyfolders, deleteall
from components.search import findpaths, findname, readall, countfiles, countfolders
from sys import argv
from os import getcwd

def set_path(command):
    if command[0] == 'path':
        if len(command) > 1:
            path = command[1]
            print(f'Path Set To: {path}')
            return path
        else:
            print('Please Specify Path')
    return None

def execute_count(command, path):
    if command[0] == 'count':
        if len(command) > 1:
            if command[1] == "files":
                print(f'{countfiles(where=path)} files')
            elif command[1] == 'folders':
                print(f'{countfolders(where=path)} folders')   
            elif command[1] == 'all':
                print([
                    f'{countfiles(where=path)} files',
                    f'{countfolders(where=path)} folders'
                ])
        else:
            print('Please Specify Type')

def execute_search(command, path):
    if command[0] == 'find' and len(command) >= 3:
        pattern = command[2]
        if command[1] == 'path':
            print(findpaths(pattern=pattern, where=path))
        elif command[1] == 'name':
            print(findname(pattern=pattern, where=path))
        elif command[1] == 'content':
            print(readall(pattern=pattern, where=path))
        elif command[1] == 'all':
            print([
                readall(pattern=pattern, where=path),
                findpaths(pattern=pattern, where=path)
            ])
        else:
            print('Please Specify Search Item')
    else:
        print('Please Specify Search Item')

def remove_empty_folders(command, path):
    if command[0] == 'rmef':
        print(deleteallemptyfolders(where=path))

def execute_delete(command, path):
    if command[0] == 'delete' and len(command) > 1:
        print(deleteall(pattern=command[1], where=path))

def process_commands(path):
    while True:
        text = input('/// ')
        if not text:
            break
        tokens = text.split()
        execute_count(tokens, path)
        execute_search(tokens, path)
        execute_delete(tokens, path)
        remove_empty_folders(tokens, path)

def main():
    if len(argv) > 1:
        tokens = argv[1:]
        current_path = set_path(tokens) or getcwd()
        process_commands(current_path)
    else:
        print('''Command
├── [set] path <directory>
│   └── Sets the current working directory for operations.
│
├── count <type>
│   ├── files
│   │   └── Counts the number of files in the specified directory.
│   ├── folders
│   │   └── Counts the number of folders in the specified directory.
│   └── all
│       └── Counts the number of both files and folders in the specified directory.
│
├── find <criterion> <pattern>
│   ├── path
│   │   └── Searches for paths matching the specified pattern.
│   ├── name
│   │   └── Searches for files/folders names matching the specified pattern.
│   ├── content
│   │   └── Searches for file content matching the specified pattern.
│   └── all
│       └── Searches for path and content matching the specified pattern.
│
├── delete <pattern>
│   └── Deletes all items matching the specified pattern in the directory.
│
└── rmef
    └── Remove all empty folders in the specified directory.''')

if __name__ == '__main__':
    main()