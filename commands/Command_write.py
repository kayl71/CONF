from Command import Command

class Command_write(Command):

    @property
    def name(self) -> str:
        return "write"
    
    @property
    def decsription(self) -> str:
        return "Создание файла с текстом"
    
    def excecute(self, args, stdin, stdout, stderr, params, tools):
        file_name = ""
        text = ""

        stdin_text = stdin.read()
        stdin.seek(0)
        if len(stdin_text) > 0:
            text = stdin_text
        if len(args) >= 1:
            file_name = args[0]
        else:
            stderr.write('No file name to write')
            return 1
        if len(args) >= 2 and len(stdin_text) == 0:
            for arg in args:
                text += str(arg) + ' '
        vfs = tools['VFS']
        if vfs.contain_file(file_name):
            stderr.write('File with name ' + file_name + ' already exists. ZIP does not support file overwriting')
            return 1
        
        vfs.add_file(file_name, text)
        
        return 0
