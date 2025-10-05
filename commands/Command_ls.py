from Command import Command

class Command_ls(Command):

    @property
    def name(self) -> str:
        return "ls"
    
    @property
    def decsription(self) -> str:
        return "Выводит содержимое директории"
    
    def excecute(self, args, stdin, stdout, stderr, params, tools):
        dir_current = params['PWD']
        ls_res = tools['VFS'].get_files_in_dir(dir_current) + tools['VFS'].get_dirs_in_dir(dir_current)
        ls_text = ""
        for file in ls_res:
            ls_text += file + '\n'
        stdout.write(ls_text)