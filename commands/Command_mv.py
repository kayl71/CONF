from Command import Command

class Command_mv(Command):

    @property
    def name(self) -> str:
        return "mv"
    
    @property
    def decsription(self) -> str:
        return "Перемещает файл или переименовывает его"
    
    def excecute(self, args, stdin, stdout, stderr, params, tools):
        if len(args) < 2:
            stderr.write("Too few arguments")
            return 1
        vfs = tools['VFS']
        file_name = args[0]
        full_file_name = params['PWD'] + '/' + file_name
        new_name = args[1]
        full_new_name = params['PWD'] + '/' + new_name
        if not vfs.contain_file(full_file_name):
            stderr.write(full_file_name + ': no such file')
            return 1
        if vfs.contain_file(full_new_name):
            stderr.write(full_file_name + ': already have that file')
            return 1
        text = vfs.read_file(full_file_name)
        vfs.delete_files_and_dirs([full_file_name])
        vfs.add_file(full_new_name, text)    

        return 0