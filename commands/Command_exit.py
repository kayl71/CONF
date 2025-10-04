from Command import Command

class Command_exit(Command):

    @property
    def name(self) -> str:
        return "exit"
    
    @property
    def decsription(self) -> str:
        return "Завершает работу эмулятора"
    
    def excecute(self, args, stdin, stdout, stderr, params):
        params['RUNNING'] = "False"
        return 0