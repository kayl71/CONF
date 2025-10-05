from Command import Command
from datetime import date

class Command_date(Command):

    @property
    def name(self) -> str:
        return "date"
    
    @property
    def decsription(self) -> str:
        return "Вывод текущей даты"
    
    def excecute(self, args, stdin, stdout, stderr, params, tools):
        stdout.write(str(date.today()))
        return 0
