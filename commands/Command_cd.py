from Command import Command

class Command_cd(Command):

    @property
    def name(self) -> str:
        return "cd"
    
    @property
    def decsription(self) -> str:
        return "Перемещение в другую директорию"
    
    def excecute(self, args, stdin, stdout, stderr, params):
        return 0