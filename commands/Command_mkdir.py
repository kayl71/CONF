from Command import Command

class Command_mkdir(Command):

    @property
    def name(self) -> str:
        return "mkdir"
    
    @property
    def decsription(self) -> str:
        return "Создает новую папку"
    
    def excecute(self, args, stdin, stdout, stderr, params, tools):
        dir_current = params['PWD']
        vfs = tools['VFS']
        dir_name = args[0]
        if vfs.contain_dir(dir_current + '/' + dir_name):
            stderr.write('Already have dir ' + dir_name)
            return 1
        vfs.add_dir(dir_current + '/' + dir_name)

        return 0