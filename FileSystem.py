import uuid

class Folder:
    def __init__(self, name, parent_dir=None):
        self.id = uuid.uuid4()
        self.name = name
        self.dir = []
        self.files = []
        self.parent_dir = parent_dir

class File:
    def __init__(self, name, content=''):
        self.name = name
        self.content = list(content)

class FileSystem:
    def __init__(self, name =''):
        self.folder = Folder(name)
        self.root = self.folder

    # get the current working directory
    def current_dir(self): 
        return self.folder.name

    # create a new directory
    def new_dir(self, name):
        dir_size = self.folder.dir
        for i in range(len(dir_size)):
            if dir_size[i].name == name:
                return 'Directory Name Exists, Unable to create new directory'
        dir_size.append(Folder(name, self.folder))
        return 'Success'

    # get the folder names in directory
    def dir_content(self):
        arr = []
        folder = self.folder
        for i in range(len(folder.dir)):
            arr.append(folder.dir[i].name)

        for i in range(len(folder.files)):
            arr.append(folder.files[i].name)

        return arr
    
    # delete directory if empty else return error message
    def dir_remove(self):
        if len(self.folder.dir) == 0 and len(self.folder.files) == 0:
            parent_dir = self.folder.parent
            pop_val = parent_dir.dir
            pop_val.pop(self.folder)
            self.folder = parent_dir
            return 'Success'
        else:
            return 'Error, Can"t Delete: There are existing folders or files in current directory'

fileSystem = FileSystem()
'''while True:
    user_input = input("Enter a command: ")
    input_split = user_input.split(' ')
    if user_input == "exit":
        break
    elif input_split[0] == 'getCurrent':
        print(fileSystem.current_dir())
    else:
        break'''
print(fileSystem.folder.id)        

'''
To Add Later: 
Creation Time
Last Modified Time
Last Access Time
Read Permissions
Multiple Users?'''