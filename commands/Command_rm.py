from Command import Command

class Command_rm(Command):

    @property
    def name(self) -> str:
        return "rm"
    
    @property
    def decsription(self) -> str:
        return "Удаляет файл"
    
    def excecute(self, args, stdin, stdout, stderr, params, tools):
        file_names_list = []
        for arg in args:
            file_names_list.append(params['PWD'] + '/' + arg)
        tools['VFS'].delete_files_and_dirs(file_names_list)
        return 0