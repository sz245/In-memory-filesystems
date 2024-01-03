from folder import Folder

class FileSystem:
    def __init__(self, name =''):
        self.folder = Folder(name)
        self.root = self.folder

    # get the current working directory path
    def current_dir(self): 
        path = ''
        traversePath = self.folder
        while traversePath:
            print(traversePath.name, path)
            path = '/' + self.folder.name + path
            traversePath = traversePath.parent_dir
        return path

    # create a new directory
    def new_dir(self, name):
        dir_size = self.folder.dir
        for i in range(len(dir_size)):
            if dir_size[i].name == name:
                return "Error: Directory Name Exists, Unable to create new directory"
        dir_size.append(Folder(name, self.folder))
        return "Success"

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
    def dir_remove(self, name):
        
        if len(self.folder.dir) == 0 and len(self.folder.files) == 0:
            parent_dir = self.folder.parent
            pop_val = parent_dir.dir
            pop_val.pop(self.folder)
            self.folder = parent_dir
            return "Success"
        else:
            return "Error, Can't Delete: There are existing folders or files in current directory"
'''
 elif input_split[0].lower() == "path" and len(input_split) == 1:
        print(fileSystem.current_dir())
    elif input_split[0].lower() == "find" and len(input_split) == 2:
        print(fileSystem.new_dir(input_split[1]))'''