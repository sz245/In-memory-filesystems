class Folder:
    def __init__(self, name, parent_dir=None):
        self.name = name
        self.parent_dir = parent_dir
        self.dir = []
        self.files = []

'''

    elif input_split[0].lower() == "makedir" and len(input_split) == 2:
        print(fileSystem.new_dir(input_split[1]))
    elif input_split[0].lower() == "listdir" and len(input_split) == 1:
        print(fileSystem.dir_content())
    elif input_split[0].lower() == "deletedir" and len(input_split) == 2:
        print(fileSystem.new_dir(input_split[1]))
    elif input_split[0].lower() == "changedir" and len(input_split) == 2:
        print(fileSystem.new_dir(input_split[1]))

    elif input_split[0].lower() == "makefile" and len(input_split) == 2:
        print(fileSystem.new_dir(input_split[1]))
    elif input_split[0].lower() == "deletefile" and len(input_split) == 2:
        print(fileSystem.new_dir(input_split[1]))
        
    elif input_split[0].lower() == "movefile" and len(input_split) == 2:
        print(fileSystem.new_dir(input_split[1]))'''