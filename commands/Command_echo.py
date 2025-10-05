from Command import Command

class Command_echo(Command):

    @property
    def name(self) -> str:
        return "echo"
    
    @property
    def decsription(self) -> str:
        return "Выводит переданные аргументы"
    
    def excecute(self, args, stdin, stdout, stderr, params, tools):
        stdin.seek(0)
        if stdin.read():
            stdin.seek(0)
            stdout.write(stdin.read())
            return 0
        
        stdin.seek(0)
        stdout.write(" ".join(args))
        return 0