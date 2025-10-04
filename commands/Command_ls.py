from Command import Command

class Command_ls(Command):

    @property
    def name(self) -> str:
        return "ls"
    
    @property
    def decsription(self) -> str:
        return "Выводит содержимое директории"
    
    def excecute(self, args, stdin, stdout, stderr, params):
        return 0