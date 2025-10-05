from Command import Command

class Command_head(Command):

    @property
    def name(self) -> str:
        return "head"
    
    @property
    def decsription(self) -> str:
        return "Выводит содержимое файла"
    
    def excecute(self, args, stdin, stdout, stderr, params, tools):
        file_name = args[0]
        num_lines = 5
        if len(args) > 1 and args[1].isdigit():
            num_lines = int(args[1])
        vfs = tools['VFS']
        full_file_name = params['PWD'] + '/' + file_name
        if not vfs.contain_file(full_file_name):
            stderr.write(full_file_name + ': No such file')
            return 1
        text = vfs.read_file(full_file_name)
        text_splitted = text.splitlines()
        for i in range(min(len(text_splitted), num_lines)):
            stdout.write(text_splitted[i] + '\n')