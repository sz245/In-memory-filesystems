from fileSystem import FileSystem

fileSystem = FileSystem()
while True:
    user_input = input("Enter a command: ")
    input_split = user_input.split(' ')
    print(input_split)
    if user_input.lower() == "exit":
        break
    elif input_split[0].lower() == "path" and len(input_split) == 1:
        print(fileSystem.current_dir())
    elif input_split[0].lower() == "find" and len(input_split) == 2:
        print(fileSystem.new_dir(input_split[1]))
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
    elif input_split[0].lower() == "listfile" and len(input_split) == 1:
        print(fileSystem.new_dir(input_split[1]))
    elif input_split[0].lower() == "writefile" and len(input_split) == 2:
        print(fileSystem.new_dir(input_split[1]))
    elif input_split[0].lower() == "deletefile" and len(input_split) == 2:
        print(fileSystem.new_dir(input_split[1]))
    elif input_split[0].lower() == "movefile" and len(input_split) == 2:
        print(fileSystem.new_dir(input_split[1]))
    else:
        print("Error: Invalid Command")

'''
To Add Later: 
Creation Time
Last Modified Time
Last Access Time
Read Permissions
Multiple Users?'''