import uuid

class File:
    def __init__(self, name, content=''):
        self.id = uuid.uuid4()
        self.name = name
        self.content = list(content)
    
    def list_content(self):
        return self.content

    def write(self, new_content):
        self.content += list(new_content)
        return self.content
'''
         elif input_split[0].lower() == "listfile" and len(input_split) == 1:
        print(fileSystem.new_dir(input_split[1]))
    elif input_split[0].lower() == "writefile" and len(input_split) == 2:
        print(fileSystem.new_dir(input_split[1]))'''